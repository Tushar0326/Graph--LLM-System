from rest_framework.decorators import api_view
from rest_framework.response import Response
from .graph import build_graph
from django.db import connection
from .llm import generate_sql


# ✅ Graph API
@api_view(["GET"])
def get_graph(request):
    G = build_graph()

    nodes = []
    edges = []

    for node, attr in G.nodes(data=True):
        nodes.append([node, attr])

    for source, target, attr in G.edges(data=True):
        edges.append([source, target, attr])

    return Response({
        "nodes": nodes,
        "edges": edges
    })


# ✅ Query API (LLM part)
@api_view(["POST"])
def query_data(request):
    user_query = request.data.get("query")

    # Guardrail
    if not any(word in user_query.lower() for word in ["order", "customer"]):
        return Response({
            "error": "This system only supports dataset queries."
        })

    sql = generate_sql(user_query)

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
    except Exception as e:
        return Response({
            "error": str(e),
            "sql": sql
        })

    return Response({
        "sql": sql,
        "data": rows
    })

@api_view(["POST"])
def query_data(request):
    user_query = request.data.get("query")

    try:
        sql = generate_sql(user_query)

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

        return Response({
            "sql": sql,
            "data": rows
        })

    except Exception as e:
        print("ERROR:", str(e))  # 👈 debug in terminal

        return Response({
            "error": "LLM or DB failed",
            "details": str(e)
        }, status=500)

def format_response(query, rows):
    if "order" in query.lower():
        return f"Found {len(rows)} orders in the system."

    if "customer" in query.lower():
        return f"There are {len(rows)} customers."

    return f"Query returned {len(rows)} results."


@api_view(["POST"])
def query_data(request):
    user_query = request.data.get("query")

    if not user_query:
        return Response({"error": "Query is required"}, status=400)

    try:
        sql = generate_sql(user_query)

        # Safety fix
        sql = sql.replace("orders", "core_order")
        sql = sql.replace("customers", "core_customer")

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

        answer = format_response(user_query, rows)

        return Response({
            "answer": answer,
            "sql": sql,
            "data": rows
        })

    except Exception as e:
        return Response({
            "error": str(e)
        }, status=500)