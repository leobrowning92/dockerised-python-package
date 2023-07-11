from pathlib import Path
import networkx as nx


def load_file_input(path: Path):
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File {path} not found")
        return {}

    lookup = {}

    for l in lines:
        values = [v.strip() for v in l.split(",")]
        lookup[values[0]] = values[1:]

    return lookup


def construct_digraph(lookup: dict) -> nx.DiGraph:
    g = nx.convert.from_dict_of_lists(lookup, create_using=nx.DiGraph)
    return g
