import numpy as np
import gaussian_elimination as ge

def get_A(n):
    row_0=[2, 1]
    for j in range(n-1):
        row_0.append(0)
    lastrow = row_0[::-1]
    A = np.zeros((n-1,n+1))
    i = 0
    while i < n-2:
        for row in A:
            row[i] = 1
            row[i+1] = 4
            row [i+2] = 1
            i += 1
    A = np.vstack((row_0,A))
    A = np.vstack((A, lastrow))
    A= np.asmatrix(A)
    return A

def get_b(n, f):
    t = np.linspace(0, n, n+1)
    y = f(t)
    b = np.empty((0,1))
    for i in range(n+1):
        if i == 0:
            line = float(3*(y[1]-y[0]))
        elif i == (n):
            line = float(3*(y[n]-y[n-1]))
        else:
            #print 'y[i+1]', y[i+1], 'y[i-1]',y[i-1]
            line = float(3*(y[i+1]-y[i-1]))
        b=np.vstack((b, line))

    b = np.asmatrix(b)
    return b

n = 6
f = lambda x: x**2
A = get_A(n)
print 'A\n', A
b = get_b(n,f)
print 'b\n', b
# A1 = np.matrix('0.0 3.0 2.0 1.0; 4.0 0.0 7.0 5.0; 8.0 2.0 0.0 2.0; 0.0 1.0 2.0 0.0')
# b1 = np.matrix('-3.0; 2.0; -2.0; -5.0')
# x = ge.gaussian_elimination(A1, b1)
# print 'x', x
# print 'residual', np.linalg.norm(A1*x- b1)**2

# D = ge.gaussian_elimination(A,b)
# print 'D', D
# print type(D[1])
# print 'residual', np.linalg.norm(A*D-b)**2

# print 'a', A
# print 'b', b
# print 'D', D
# print 'residual:', np.linalg.norm(A*D - b)**2
