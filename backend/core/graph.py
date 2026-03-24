import networkx as nx
from core.models import Customer, Order

def build_graph():
    G = nx.DiGraph()

    # Nodes
    for customer in Customer.objects.all():
        G.add_node(f"C{customer.id}", type="customer", name=customer.name)

    for order in Order.objects.all():
        G.add_node(f"O{order.id}", type="order")

    # Edges
    for order in Order.objects.all():
        G.add_edge(
            f"C{order.customer.id}",
            f"O{order.id}",
            relation="PLACED"
        )

    return G