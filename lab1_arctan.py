#estimate pi via taylor series of arctan x
import numpy as np

def tspil(n):
  sum = 0
  denom = 1.0
  for i in range(n):
    #print i
    sign = (-1)**i
    #print 'sign', sign
    term = sign/denom
    #print 'term', term
    denom = denom + 2.0
    sum = sum + term
  pi = sum*4
  return pi


print '5 terms', tspil(5)
print '10 terms', tspil(10)
print '1000 terms', tspil(1000000)
