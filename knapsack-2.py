#!/usr/bin/python

# Knapsack algorithm

# This file describes a knapsack instance, and it has the following format:
#
# [knapsack_size][number_of_items]
# [value_1] [weight_1]
# [value_2] [weight_2]
#

# For example, the third line of the file is "50074 834558", indicating that the second item 
# has value 50074 and size 834558, respectively. As before, you should assume that item weights 
# and the knapsack capacity are integers.
#
# This instance is so big that the straightforward iterative implemetation uses an infeasible 
# amount of time and space. So you will have to be creative to compute an optimal solution. 
# One idea is to go back to a recursive implementation, solving subproblems --- and, of course, 
# caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure 
# to think about appropriate data structures for storing and looking up solutions to subproblems

# NOTE: just solved limiting the dictionary size (lack of time)
# TODO: improve the code to decrease the running time

# Get the value of the optimal solution.

# load contents of text file into a list numList
NUMLIST_FILENAME = "data/knapsack_big.txt" # optimal value: 4243395

inFile = open(NUMLIST_FILENAME, 'r')

knapsack_size = 0
number_of_items = False
items = []
A = { 0:{} } 

for f in inFile:
    if(number_of_items == False):
        knapsack_size, number_of_items = map(int, f.split())
    else:
        value, weight = map(int, f.split())
        items.append([value, weight])

# initializing 
for x in range(0, knapsack_size + 1):
    A[0][x] = 0

for i in range(1, number_of_items + 1):
    # limiting dictionary size
    if i > 1:
        del A[i-2]
    if i not in A:
        A[i] = {}
    for x in range(0, knapsack_size + 1):
        option_a = A[i-1][x]
        value = items[i-1][0]
        weight = items[i-1][1]
        if x - weight >= 0 and x - weight <= knapsack_size:
            option_b = A[i-1][x-weight] + value
        else:
            option_b = 0
        if option_a >= option_b:
            A[i][x] = option_a
        else:
            A[i][x] = option_b

# optimal value
print 'Optimal Value: ' + str(A[number_of_items][knapsack_size])
