#!/usr/bin/python

# Greedy Algorithm to schedule jobs in decreasing order of the ratio

# Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order 
# of the ratio (weight/length). In this algorithm, it does not matter how you break ties. 
# You should report the sum of weighted completion times of the resulting schedule. 
# --- a positive integer. 

# load contents of text file into a list numList
NUMLIST_FILENAME = "data/mwsct.txt" # Ratio: 67311454237
# NUMLIST_FILENAME = "data/tests/mwsct-test-1.txt" # Ratio: 31814
# NUMLIST_FILENAME = "data/tests/mwsct-test-2.txt" # Ratio: 60213
# NUMLIST_FILENAME = "data/tests/mwsct-test-3.txt" # Ratio: 674634

inFile = open(NUMLIST_FILENAME, 'r')

jobs = []
num_jobs = 0

for f in inFile:
    if(num_jobs == 0):
        num_jobs = int(f.strip())
    else:
        weight, length = map(int, f.split())
        ratio = float(weight)/float(length)
        jobs.append([weight, length, ratio])

def sumWeightedCompletionTimes(myList):
    global jobs
    '''given a list with format [job_weight, job_length, weight/length]
    first order them by decreasing order of ratio weight/length.
    Return the sum of completion times.'''
    # using sorted method because is stable 
    # (it guarantees the relative order of elements that compare to equal)
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    completion_time = 0
    sum_weighted_completion_time = 0
    for job in jobs:
        completion_time += job[1]
        sum_weighted_completion_time += job[0] * completion_time
    return sum_weighted_completion_time


sum_weighted_completion_time = sumWeightedCompletionTimes(jobs)
print 'result: ' +  str(sum_weighted_completion_time)
