import numpy as np
import gaussian_elimination as ge
import parse_netlist as parse
#
def generate_G(R,n):
    # find number of nodes by finding maximum node number
    G = np.zeros((n, n), dtype = np.float64)
    # fill in diagonals
    for i in range(len(R)):
        #print 'i', i
        for res in R:
            #res = R[i]
            #print 'this resistor: source & dest', res.src, res.dst
            #print type(res.src)
            if i+1 == res.src or i+1 == res.dst:
                G[i, i] += 1/res.value

                #print 'Adding resistor to location', i, i
            for j in range(len(R)):

                if i == j:
                    pass
                else:
                    #print 'i,j', i+1,j+1
                    if (i+1 ==res.src and j+1 == res.dst) or (j+1 ==res.src and i+1 == res.dst):
                        #print 'hey'
                        G[i, j] -= 1/res.value

    return G
# def generate_G(R, n):
#     gmat = np.zeros((n, n), dtype = np.float64)
#     for res in R:
#         src = res.src
#         dst = res.dst
#         # print '{}'.format(res.name)
#         # print 'source = {}\tdestination = {}'.format(src,dst)
#         # print 'value = {}'.format(res.value)
#         if src != 0:
#             gmat[src-1,src-1] = gmat[src-1,src-1] + 1.0/res.value
#         if dst != 0:
#             gmat[dst-1,dst-1] = gmat[dst-1,dst-1] + 1.0/res.value
#         if src != 0 and dst != 0:
#             gmat[src-1,dst-1] = -1.0/res.value
#             gmat[dst-1,src-1] = -1.0/res.value
#
#         #print 'gmat = {}'.format(gmat)
#         return gmat

def generate_B(voltages, n):
    #print voltages
    m = len(voltages)
    B = np.zeros((n,m))
    for i in range(n):  #run through nodes
        for j in range(len(voltages)): #run through voltages
            v = voltages[j]
            if v.src == i+1:
                B[i,j] = -1
            elif v.dst == i+1:
                B[i,j] = 1
            else:
                B[i,j] = 0
    return B

def generate_C(voltages, n):
    m = len(voltages)
    C = np.zeros((m,n))
    for i in range(len(voltages)):
        v = voltages[i]
        for j in range(n):
            if v.src == j + 1:
                C[i,j] = -1
            elif v.dst == j + 1:
                C[i,j] = 1
            else:
                C[i,j] = 0
    return C


    # fill in off-diagonals
#
# def solve_netlist(V,I,R,N):
#     G = generate_G(R)
#     B = generate_B()
#     return A, x, b

def generate_i(I,n):
    i = np.zeros((n,1), dtype=np.float64)
    for cur in I:
        src = cur.src
        dst = cur.dst
        value = cur.value
        for node in range(1,n+1):
            if src == node:
                i[node-1,0] = -value
            elif dst == node:
                i[node-1,0] = value
    return i

def generate_e(V,m):
    e = np.zeros((m,1), dtype=np.float64)
    for v_num in range(0,m):
        volt = V[v_num]
        value = volt.value
        e[v_num-1,0] = value
    return e

def generate_A(G,C,B,n,m):
    D = np.zeros((m,m), dtype=np.float64)
    G_C = np.vstack((G,C))
    B_D = np.vstack((B,D))
    A = np.hstack((G_C,B_D))
    return A

def generate_z(i,e):
    z = np.vstack((i,e))
    return z

def generate_x(A,z):
    x = ge.gaussian_elimination(A,z)
    return x

def solve_netlist(V,I,R,N,M):
    C = generate_C(V,N)
    G = generate_G(R,N)
    print 'G ='
    print G
    B = generate_B(V,N)
    i = generate_i(I,N)
    e = generate_e(V,M)
    A = generate_A(G,C,B,N,M)
    z = generate_z(i,e)
    x = generate_x(A,z)
    print 'C ='
    print C
    print 'G ='
    print G
    print 'B ='
    print B
    print 'i ='
    print i
    print 'e ='
    print e
    return(A,x,z)

[V, I, R, N, M] = parse.parse_netlist('circuit.cir')

def main():
    [V, I, R, N, M] = parse.parse_netlist('circuit.cir')
    (A,x,z) = solve_netlist(V,I,R,N,M)
    print 'A ='
    print A
    print 'x ='
    print x
    print 'z ='
    print z

main()
