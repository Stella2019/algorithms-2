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
NUMLIST_FILENAME = "data/mwsct.txt" # diff: 69119377652
# NUMLIST_FILENAME = "data/tests/mwsct-test-1.txt" # diff: 31814
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

def sumWeightedCompletionTimes():
    global jobs
    '''given a list with format [job_weight, job_length, weight - length]
    it uses two sorts, one to order them by decreasing order of weight 
    and the other to order them in decreasing order of weight - length.
    Cause sorted function is stable we keep the equal comparision ordered
    by decreasing weight as required. Return the sum of completion times.'''
    jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    completion_time = 0
    sum_weighted_completion_time = 0
    for job in jobs:
        completion_time += job[1]
        sum_weighted_completion_time += job[0] * completion_time
    return sum_weighted_completion_time


sum_weighted_completion_time = sumWeightedCompletionTimes()
print 'result: ' + str(sum_weighted_completion_time)
