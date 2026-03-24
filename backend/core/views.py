
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .graph import build_graph

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