# E019 Lab 1
# Estimating pi

import numpy as np

# Part 1: Monte Carlo Method

def mcp(n):
    darts = np.empty([0,2])
    #create a set of darts in the 1x1 square
    circle_darts = 0
    # missed = 0
    for i in range(n):
        coords = [np.random.random(), np.random.random()]
        #darts = np.vstack((darts,coords))  #unnecessary
        circ = np.sqrt((coords[0])**2 + (coords[1])**2)
        #count how many darts fell into the unit circle
        if circ < 1:
            circle_darts = circle_darts + 1
        # else:
        #     missed = missed + 1
    pi_estimate = 4.0*(float(circle_darts)/float(n))
    return pi_estimate

#estimate_10 = mcp(10)
#estimate_100 = mcp(100)
#estimate_10000 = mcp(1000000)

# print '10 dart estimate', estimate_10
# print '100 dart estimate', estimate_100
for i in range(10):
    print '100,000,000 dart estimate', mcp(100 000 000)
