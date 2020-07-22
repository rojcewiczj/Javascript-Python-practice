import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    color_dict = {}
    con_dict = {}
    connections = []
    visted = []
    for i in range(0, len(graph_from)):
        connections.append([graph_from[i], graph_to[i]])
   
        if graph_from[i] not in con_dict:
            con_dict[graph_from[i]] = [graph_to[i]]
        else:
            con_dict[graph_from[i]].append(graph_to[i])
   
        if graph_to[i] not in con_dict:
            con_dict[graph_to[i]] = [graph_from[i]]
        else:
            con_dict[graph_to[i]].append(graph_to[i])
    inc = 0
    for array in connections:
        print(inc)
        if array[0] not in color_dict:
            color_dict[array[0]] = ids[inc]
            inc += 1
             
        if array[1] not in color_dict:
            color_dict[array[1]] = ids[inc]
            inc += 1

    queue = []
    path = []
    trav_visited = [1,]
    current_node = 1
    if color_dict[current_node] == val:
        for node in con_dict[current_node]:
            if color_dict[node] == color_dict[current_node]:
                path.append(node)
                break
            