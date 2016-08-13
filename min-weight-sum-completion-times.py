#!/usr/bin/python

# Greedy Algorithm for minimizing the weighted sum of completion times

# This file describes a set of jobs with positive and integral weights and lengths. It has the format
#
# [number_of_jobs]
# [job_1_weight] [job_1_length]
# [job_2_weight] [job_2_length]
#
# For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.
#
# You should NOT assume that edge weights or lengths are distinct.
#
# Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order 
# of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. 
# IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with 
# higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong 
# answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer. 

# load contents of text file into a list numList
# NUMLIST_FILENAME = "data/mwsct.txt" # diff: 69120458973
NUMLIST_FILENAME = "data/tests/mwsct-test-1.txt" # diff: 31814
# NUMLIST_FILENAME = "data/tests/mwsct-test-2.txt" # diff: 61545
# NUMLIST_FILENAME = "data/tests/mwsct-test-3.txt" # diff: 688647

inFile = open(NUMLIST_FILENAME, 'r')

jobs = []
num_jobs = 0

for f in inFile:
    if(num_jobs == 0):
        num_jobs = int(f.strip())
    else:
        weight, length = map(int, f.split())
        jobs.append([weight, length, weight - length])

def quicksort(myList, start, end, position):
    '''quicksort method to sort multi lists specifying 
    the position of the sortered element of inner list'''
    if start < end:
        # partition the list
        pivot = partition(myList, start, end, position)
        # sort both halves
        quicksort(myList, start, pivot-1, position)
        quicksort(myList, pivot+1, end, position)
    return myList

def partition(myList, start, end, position):
    '''partition of quicksort method to sort multi lists specifying 
    the position of the sortered element of inner list, with a small 
    modification to order equal elements by decreasing order of 
    first element of the inner list'''
    pivot = myList[start][position]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left][position] <= pivot:
            # order by greater weight if are equal
            if myList[left][position] == pivot and myList[left][0] > myList[start][0]:
                break
            left = left + 1
        while myList[right][position] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def sumWeightedCompletionTimes(myList):
    global jobs
    '''given a list with format [job_weight, job_length, weight - length]
    it uses quicksort to order them by decreasing order of weight - length.
    Return the sum of completion times.'''
    quicksort(jobs, 0, len(jobs)-1, 2)
    jobs.reverse()
    completion_time = 0
    sum_weighted_completion_time = 0
    for job in myList:
        completion_time += job[1]
        sum_weighted_completion_time += job[0] * completion_time
    return sum_weighted_completion_time


sum_weighted_completion_time = sumWeightedCompletionTimes(jobs)
print 'result: ' + str(sum_weighted_completion_time)
