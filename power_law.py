#!/usr/bin/env python
import math
import random
import optparse

def binary_search(low, high, a, k):
    mid = low + (high - low)/2
    if 1 / math.pow(mid, k) < a: 
        high = mid
    elif 1 / math.pow(mid+1, k) > a:
        low = mid
    else:
        return mid
    return binary_search(low, high, a, k)

def sample_discrete_power(k):
    a = random.random()
    i = 0
    while (1.0/math.pow(2 ** i, k)) > a:
        i += 1
    
    high = 2 ** i
    low = 2 ** (i - 1)
    return binary_search(low, high, a, k)

def run_experiment(trials, k):
    samples = []
    running_avg = []
    sum = 0
    for i in xrange(1,trials+1):
        rnd = sample_discrete_power(k)
        sum += rnd 
        samples.append(rnd)
        running_avg.append(sum/float(i))
    return running_avg, samples
        

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-t', dest='trials', default=10000, type=int)
    parser.add_option('-k', dest='k', default=1, type=int)
    parser.add_option('-f', dest='file', default='power_law.csv', type='string')
    (option, args) = parser.parse_args()
    runnig_avg, samples = run_experiment(option.trials, option.k)
    print samples

    with open(option.file, "w") as fp:
        for i,j in enumerate(runnig_avg, 1):
            fp.write("%s,%s\n" % (i,j))
        




    
