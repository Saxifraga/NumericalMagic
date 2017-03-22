import numpy as np
import gaussian_elimination as ge
import parse_netlist as parse

def generate_G(R,n):
    # find number of nodes by finding maximum node number
    G = np.zeros((n, n), dtype = np.float64)
    # fill in diagonals
    for i in range(len(R)):
        #print 'i', i
        for res in R:
            #res = R[i]
            print 'this resistor: source & dest', res.src, res.dst
            #print type(res.src)
            if i+1 == res.src or i+1 == res.dst:
                G[i, i] += 1/res.value

                print 'Adding resistor to location', i, i
            for j in range(len(R)):

                if i == j:
                    pass
                else:
                    print 'i,j', i+1,j+1
                    if (i+1 ==res.src and j+1 == res.dst) or (j+1 ==res.src and i+1 == res.dst):
                        #print 'hey'
                        G[i, j] -= 1/res.value

    return G
    # fill in off-diagonals
#
# def solve_netlist(V,I,R,N):
#     G = generate_G(R)
#     B = generate_B()
#     return A, x, b

[V, I, R, N] = parse.parse_netlist('lab2.cir')

print generate_G(R,N)
#[A, x, b] = solve_netlist(V,I,R,N)
