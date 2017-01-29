# E019 Lab 1
# Estimating pi

import numpy as np

# Part 1: Monte Carlo Method

def mcp(m,n):
    #create a set of darts in the 1x1 square

    # missed = 0
    pi_estimate = []
    for i in range(n):
        coords = np.random.random((m, 2))
        #count how many darts fell into the unit circle
        circ = (coords[:,0])**2 + (coords[:,1])**2
            # if circ < 1:    #look up np.count_nonzero
            #     circle_darts = circle_darts + 1
        circle_darts = np.count_nonzero(circ<1)
        this_guess =4.0*(float(circle_darts)/float(m))
        pi_estimate.append(this_guess)
    pi_estimate = np.mean(pi_estimate)

    return pi_estimate

#estimate_10 = mcp(10)
#estimate_100 = mcp(100)
#estimate_10000 = mcp(1000000)

# print '10 dart estimate', estimate_10
# print '100 dart estimate', estimate_100
for i in range(10):
    c = mcp(200000, 5000)
    print '\nIteration', i+1
    print 'Full estimate', c#np.round(mcp(200000,5000),3)
    print 'Rounded estimate', np.round(c,3)
