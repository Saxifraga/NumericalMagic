#estimate pi via taylor series of arctan x
import numpy as np

def tspi1(n):
  sum1 = 0
  denom = 1.0
  percent_error = 'not applicable'
  #this loop calculates + sums n terms of the maclaurin series of arctan(1)
  #it also calculates and prints the error
  for i in range(n):
    #print i
    sign = (-1)**i
    #print 'sign', sign
    term = sign/denom
    #print 'term', term
    denom = denom + 2.0
    newsum = sum1 + term
    #calculate true & approximate relative error
    #but ONLY on the last iteration
    if (i == n-1) and (i > 0):
        true_error = abs((np.pi - 4*newsum)/np.pi)*100  #true relative percent error
        print 'true relative error:', true_error, '%'
        percent_error = abs(100*((newsum-sum1)/newsum))     #approx relative percent error
        print 'approximate relative error:', percent_error, '%'
    sum1 = newsum
  pi = sum1*4
  print 'estimate of pi:', pi
  return pi

#TODO implement tspi2(n). modify the for loop in tspi1(n) to generalize to all arctans
#then implement the Machin formula


for i in range(20):
    print i+1, 'terms'
    tspi1(i+1)
    print '\n'
# true_error = abs((np.pi - 100)/np.pi)*100
# print true_error
#print '10 terms', tspi1(10)
#print '1000 terms', tspi1(1000000)
