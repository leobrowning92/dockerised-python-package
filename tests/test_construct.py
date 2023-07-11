from ball_pass import construct
from pathlib import Path


def test_load_file_input():
    fpath = Path("tests/example.txt")
    lookup = construct.load_file_input(fpath)

    assert list(lookup.keys()) == [
        "George",
        "Rick",
        "Anne",
        "Beth",
        "Sue",
    ]
    assert lookup["George"] == [
        "Beth",
        "Sue",
    ]


def test_construct_digraph(example_lookup):
    g = construct.construct_digraph(example_lookup)

    assert set(g.nodes) == {
        "George",
        "Rick",
        "Anne",
        "Beth",
        "Sue",
    }
    assert set(g.edges) == {
        ("George", "Beth"),
        ("George", "Sue"),
        ("Rick", "Anne"),
        ("Anne", "Beth"),
        ("Beth", "Anne"),
        ("Beth", "George"),
        ("Sue", "Beth"),
    }
