#!/home/user/.local/bin/checkio --domain=py run node-subnetworks

# Sometimes damaged nodes are unrecoverable. In that case, people that were connected to the crushed node must migrate to another district while administration attempts to fix the node.
# 
# But if a crushed node disconnects multiple districts from one another, then the network splits into two sub-networks and every sub-network should have their own Mayor. And Mayors must use pigeons for mailing between each other. In that case, when the network is split you don’t need hundreds of pigeons.
# 
# Your mission is to figure out how many Mayors you need to control the entire city when some nodes are crushed. In other words, you need to figure out how many sub-networks will be formed after some nodes are crush and not recovered.
# 
# Input:Two arguments: the network structure (as a list of connections between the nodes) and the list of crashed nodes.
# 
# Output:Int. The amount of sub-networks formed after some nodes were crushed.
# 
# 
# END_DESC

import numpy as np


def subnetworks(net, crushes):
    node_list = sorted(set("".join([j for j in ["".join(i) for i in net]])))
    network_before = np.zeros(len(node_list) ** 2, dtype=int).reshape(
        len(node_list), len(node_list)
    )
    edge_list_x = [j[0] for j in ["".join(i) for i in net]]
    edge_list_y = [j[1] for j in ["".join(i) for i in net]]
    for i, j in zip(edge_list_x, edge_list_y):
        x = node_list.index(i)
        y = node_list.index(j)
        network_before[x, y] = 1
        network_before[y, x] = 1
    delete_node = [node_list.index(i) for i in crushes]
    network_after = np.delete(np.delete(network_before, delete_node, 0), delete_node, 1)
    result = []
    for i in range(len(network_after[0, :])):
        result.append(sum([j for j in network_after[:, i]]))
    single = len([i for i in result if i == 0])
    pair = len([i for i in result if i == 1]) // 2
    return single + pair


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([["A", "B"], ["B", "C"], ["C", "D"]], ["B"]) == 2, "First"
    assert (
        subnetworks([["A", "B"], ["A", "C"], ["A", "D"], ["D", "F"]], ["A"]) == 3
    ), "Second"
    assert subnetworks([["A", "B"], ["B", "C"], ["C", "D"]], ["C", "D"]) == 1, "Third"
    print("Done! Check button is waiting for you!")