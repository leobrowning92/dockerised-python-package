import pytest
import networkx as nx


@pytest.fixture
def example_lookup():
    return {
        "George": [
            "Beth",
            "Sue",
        ],
        "Rick": [
            "Anne",
        ],
        "Anne": [
            "Beth",
        ],
        "Beth": [
            "Anne",
            "George",
        ],
        "Sue": [
            "Beth",
        ],
    }


@pytest.fixture
def example_digraph():
    g = nx.DiGraph()
    g.add_nodes_from(
        [
            "George",
            "Rick",
            "Anne",
            "Beth",
            "Sue",
        ]
    )
    g.add_edges_from(
        [
            ("George", "Beth"),
            ("George", "Sue"),
            ("Rick", "Anne"),
            ("Anne", "Beth"),
            ("Beth", "Anne"),
            ("Beth", "George"),
            ("Sue", "Beth"),
        ]
    )
    return g


@pytest.fixture
def complete_digraph_factory():
    def _f(n):
        return nx.DiGraph(nx.generators.classic.complete_graph(n))

    return _f


@pytest.fixture
def complete_lookup_factory(complete_digraph_factory):
    def _f(n):
        g = complete_digraph_factory(n)
        return nx.convert.to_dict_of_lists(g)

    return _f
