
#estimate pi via taylor series of arctan x
import numpy as np

def tspi2(n):
  sum1 = 0
  sum2 = 0
  denom = 1.0
  exponent = 1
  for i in range(n):
    #print i
    sign = (-1)**i
    #print 'sign', sign
    term1 = (sign*0.2)**(exponent)/denom
    term2 = (sign*1.0/239)**(exponent)/denom
    #print term1
    #print 'term', term
    denom = denom + 2.0
    exponent = exponent + 2.0
    sum1 = sum1 + term1
    sum2 = sum2 + term2
  pi_est = sum1*16-sum2*4    
  true_error = abs(np.pi - pi_est)
  true_relative_error = true_error/np.pi
  true_relative_percent_error = true_relative_error*100
  print "n =", n
  print "pi estimate =", pi_est
  print "true relative error =", true_relative_percent_error, "%"
  return pi_est

for n in range(1,21):
  current_approx = tspi2(n)
  if n > 1: 
    approximate_relative_error = abs(100*(current_approx-prev_approx)/current_approx)
    print "approximate relative error =", approximate_relative_error, "%"
  print ''
  prev_approx = current_approx

