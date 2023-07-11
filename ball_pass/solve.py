import networkx as nx
from ball_pass import construct


def nx_prune_digraph(digraph: nx.DiGraph) -> nx.Graph:
    """Prune graph to include only bidirectional edges"""
    g = digraph.to_undirected(reciprocal=True)
    return g


def nx_solve(lookup: dict) -> int:
    """Solve the ball-passing problem using networkx"""
    digraph = construct.construct_digraph(lookup)
    g = nx_prune_digraph(digraph)
    largest_cc = max(nx.connected_components(g), key=len)
    return len(largest_cc)


def manual_solve(lookup: dict) -> int:
    """Solve the ball-passing problem in plain python.

    This is for the purposes of complexity analysis.

    This uses a depth-first search to find connected components.

    Note:
        The check for bidirectionality is implemented at the same
        time as edge traversal. Only bidirectional edges are traversed.
    """
    traversed_nodes = set([])
    connected_sets = []
    for n in lookup.keys():
        if not n in traversed_nodes:
            connected_set = traverse(n, set([]), lookup)
            traversed_nodes = traversed_nodes | connected_set
            connected_sets.append(connected_set)
    return len(max(connected_sets, key=len))


def traverse(n, connected_set, lookup):
    print(n)
    connected_set.add(n)
    for seen_node in lookup[n]:
        # split out for clarity in toy problem
        bidirectional = n in lookup[seen_node]
        if bidirectional and seen_node not in connected_set:
            traverse(seen_node, connected_set, lookup)
    return connected_set
