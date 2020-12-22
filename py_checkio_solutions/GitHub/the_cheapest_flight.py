#!/usr/local/bin/checkio --domain=py run the-cheapest-flight

from typing import List
import itertools
import numpy as np
from scipy.sparse.csgraph import (
    shortest_path,
    dijkstra,
)
from scipy.sparse import csr_matrix


def cheapest_flight(costs: List, a: str, b: str) -> int:
    node_list = sorted(
        set([i for i in itertools.chain.from_iterable(costs) if isinstance(i, str)])
    )
    cost_array = np.zeros((len(node_list), len(node_list)))
    for i in costs:
        first = node_list.index(i[0])
        second = node_list.index(i[1])
        cost_array[first, second] = i[2]
        cost_array[second, first] = i[2]
    csr = csr_matrix(cost_array)
    start = node_list.index(a)
    goal = node_list.index(b)
    lowest_cost = shortest_path(csr, method="D", indices=[start])[0][goal]
    if lowest_cost == np.inf:
        return 0
    return int(lowest_cost)


if __name__ == "__main__":
    print("Example:")
    print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")
        == 70
    )
    assert (
        cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A")
        == 70
    )
    assert (
        cheapest_flight(
            [
                ["A", "C", 40],
                ["A", "B", 20],
                ["A", "D", 20],
                ["B", "C", 50],
                ["D", "C", 70],
            ],
            "D",
            "C",
        )
        == 60
    )
    assert (
        cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F")
        == 0
    )
    assert (
        cheapest_flight(
            [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
        )
        == 25
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")
