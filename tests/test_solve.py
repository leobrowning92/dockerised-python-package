from ball_pass import solve
import pytest


def test_prune_digraph(example_digraph):
    g = solve.nx_prune_digraph(example_digraph)
    print(g.adj)
    assert set(g.nodes) == {
        "George",
        "Rick",
        "Anne",
        "Beth",
        "Sue",
    }
    assert set(g.edges) == {
        ("George", "Beth"),
        ("Anne", "Beth"),
    }


@pytest.mark.parametrize("solve_method", [solve.nx_solve, solve.manual_solve])
def test_solve_example(solve_method, example_lookup):
    n = solve_method(example_lookup)
    assert n == 3


@pytest.mark.parametrize("n", [1, 5, 100])
@pytest.mark.parametrize("solve_method", [solve.nx_solve, solve.manual_solve])
def test_solve_complete(n, solve_method, complete_lookup_factory):
    g = complete_lookup_factory(n)
    n_calc = solve_method(g)
    assert n_calc == n

@pytest.mark.parametrize("solve_method", [solve.nx_solve, solve.manual_solve])
def test_solve_single_person(solve_method):
    lookup = {"George": []}
    n = solve_method(lookup)
    assert n == 1
