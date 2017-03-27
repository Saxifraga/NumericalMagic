import numpy as np
import gaussian_elimination as ge
import scipy.linalg
import matplotlib.pyplot as plt

'''the function get_A produces the A matrix required by the cubic spline'''

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

'''the function get_b produces the b matrix required by the cubic spline'''

def get_b(n, f, t):
    y = f(t)
    b = np.empty((0,1))
    for i in range(n+1):
        if i == 0:
            line = float(3*(y[1]-y[0]))
        elif i == (n):
            line = float(3*(y[n]-y[n-1]))
        else:
            line = float(3*(y[i+1]-y[i-1]))
        b=np.vstack((b, line))
    b = np.asmatrix(b)
    return b, y

''' the functions grab_diags and ab_row create the ab matrix specified by
the documentation for scipy.linalg.solve_banded'''

def ab_row(k,A,n):
    row = np.zeros((1,n), np.float64)
    if k == 0:
        [i,j] = [0,1]
    elif k == 1:
        [i,j] = [0,0]
    elif k ==2:
        [i,j] = [1,0]
    while j < n:
        try:
            row[0,j] = A[i,j]
        except:
            pass
        i += 1
        j += 1
    return row

def grab_diags(A,n):
    n = n + 1
    ab = np.empty((0,n))
    for k in range(3):
        row = ab_row(k, A, n)
        ab = np.vstack((ab, row))
    return ab

''' The function get_Y returns the ith interpolated point by solving for the
coefficients a,b,c,d and multiplying by the ith x vector '''

def get_Y(D,y,n,t):
    tmax = max(t)
    x = np.arange(0.0, tmax-1, 0.1)
    Y_out = np.zeros((n,1))
    for i in range(n):
        t_vec = np.zeros((4,1))
        # produce [1; t; t^2; t^3]:
        for j in range(4):
            t_vec[j,0] = (x[i+1]-x[i])**j
        # get ith set of coefficients
        a = y[i]
        b = D[i]
        c = 3*(y[i+1]-y[i]) - 2*D[i] - D[i+1]
        d = 2*(y[i]-y[i+1]) + D[i] + D[i+1]
        row = [a, b, c, d]
        # multiply to get interpolated points
        Y_out[i,0] = np.dot(row, t_vec)
    return Y_out, t


def gauss_seidel(A,b,n):
    es = 1
    lam = .2
    x = np.zeros(n+1)
    for i in range(0, n+1):
        dummy = A[i,i]
        for j in range(0, n+1):
            A[i,j]=A[i,j]/dummy
        b[i]=b[i]/dummy
    for i in range(0, n+1):
        old = x[i]
        summ = b[i]
        for j in range(0,n+1):
            if i != j:
                summ = summ - A[i,j]*x[j]
            x[i] = summ
    iter = 1
    t = True
    while t == True:
        sentinel = 1
        for i in range(0, n+1):
            old = x[i]
            summ = b[i]
            for i in range(0, n+1):
                if i != j:
                    summ = summ - A[i,j]*x[j]
        x[i] = lam*summ + (1-lam)*old
        if sentinel == 1 and x[i] != 0:
            ea = abs((x[i]-old)/x[i])*100
            if ea > es:
                sentinel = 0
        iter = iter +1
        if sentinel == 0:
            t = False
    return x

def scipy_solveband(A, b, n):
    u = 1
    l = 1
    ab = grab_diags(A, n)
    #print 'ab \n', ab
    D = scipy.linalg.solve_banded((l, u), ab,b)
    return D

n = 20
f = lambda x: .00003*(x**5) - .0013*(x**3) + .0001*(x**2) + (4)*np.sin(x)

t = np.arange(0.0, n+1, 1)

A = get_A(n)
print 'A\n', A
[b,y] = get_b(n,f,t)
#D = scipy_solveband(A, b, n)
# call other method of solving banded matrix here
D = gauss_seidel(A,b,n)
print 'length of y', len(y)
print 'length of d', len(D)
[Y, t] = get_Y(D,y,n,t)

plt.plot(t, y, 'k', label = 'control')
# plt.plot(t,y, 'bo', label = 'control pts')
plt.plot(Y, 'r+', label = 'interp pts')
plt.title('Control and Interpolated Points')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
