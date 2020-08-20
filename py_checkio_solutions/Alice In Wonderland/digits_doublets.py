#!/usr/local/bin/checkio --domain=py run digits-doublets

# .story .shadow {        float: left;        /*padding: 10px;*/        margin: 10px;        border: black;        /*box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-moz-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/        /*-webkit-box-shadow: 0 0 20px 10px rgba(0, 0, 0, 1);*/    }    .story .left {        float: left;    }    .story .right {        float: right;    }    .story .title {        font-weight: bold;        margin: 20px 0 20px 0;    }
# END_DESC

import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix


def matching(first, next):
    count = 0
    for i, j in zip(list(str(first)), list(str(next))):
        if i == j:
            count += 1
    if count == 2:
        return 1
    else:
        return 0


def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])


def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
    if i < 0:
        return []
    path.append(i)
    return path[::-1]


def checkio(numbers):
    network = np.empty(0, dtype=np.int)
    for first_num in range(len(numbers)):
        for next in numbers:
            network = np.append(network, matching(numbers[first_num], next))
    network = network.reshape(len(numbers), -1)
    d, p = shortest_path(network, return_predecessors=True)
    result = get_path(0, numbers.index(numbers[-1]), p)
    return [numbers[i] for i in result]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"