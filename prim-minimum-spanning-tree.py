#!/usr/bin/python

# Prim's minimum spanning tree algorithm

# This file describes an undirected graph with integer edge costs. It has the format
#
# [number_of_nodes] [number_of_edges]
# [one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
# [one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]

# For example, the third line of the file is "2 3 -8874", indicating that there is an edge 
# connecting vertex #2 and vertex #3 that has cost -8874.
#
# You should NOT assume that edge costs are positive, nor should you assume that they are distinct.
#
# Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the 
# overall cost of a minimum spanning tree --- an integer, which may or may not be negative 
#
# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation 
# of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, 
# try implementing a heap-based version. The simpler approach, which should already give you a 
# healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). 
# The superior approach stores the unprocessed vertices in the heap, as described in lecture. 
# Note this requires a heap that supports deletions, and you'll probably need to maintain some kind 
# of mapping between vertices and their positions in the heap.

# load contents of text file into a list numList
NUMLIST_FILENAME = "data/pmst.txt" # cost: -3612829
# NUMLIST_FILENAME = "data/tests/pmst-test-1.txt" # cost: 7

inFile = open(NUMLIST_FILENAME, 'r')

edges = []
cv = 0 # current vertex
numbers = False
included_nodes = []
tree = []
overall_cost = 0

for f in inFile:
    if(numbers == False):
        num_nodes, num_edges = map(int, f.split())
        numbers = (num_nodes, num_edges)
    else:
        node1, node2, cost = map(int, f.split())
        edges.append([node1, node2, cost])

# sorting edges by increasing order of edge cost
edges = sorted(edges, key=lambda x: x[2])

#initializing current vertex
cv = edges[0][0]

while len(included_nodes) < numbers[0]:
    if cv not in included_nodes:
        included_nodes.append(cv)
        for e in edges:
            if ((e[0] == cv and e[1] not in included_nodes) or
                    (e[0] in included_nodes and e[1] not in included_nodes)):
                overall_cost += e[2]
                cv = e[1]
                break
            elif ((e[1] == cv and e[0] not in included_nodes) or
                    (e[1] in included_nodes and e[0] not in included_nodes)):
                overall_cost += e[2]
                cv = e[0]
                break
            else: 
                continue
        
print overall_cost

# @todo: implement heaps method
