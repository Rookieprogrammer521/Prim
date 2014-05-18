def weight():
    
    pass


def adjacent(A):

    pass


def extract_min(Q):

    pass


def decrease_key(Q):

    pass


def prim(V, A, r):
    u = 0
    v = 0

    P=[None]*len(V)

    K = [999999]*len(V)

    Q=[0]*len(V)
    for u in range(len(Q)):
        Q[u] = V[u]

    K[r] = 0
    decreaseKey(Q, K)

    while len(Q) > 0:
        u = extractMin(Q)   

        Adj = adjacent(A, u)
        for v in Adj:
            w = weight(A, u, v)


            if Q.count(v)>0 and w < K[v]:
                P[v] = u
                K[v] = w
                decreaseKey(Q, K)
    return P


print ("galutinis rezultatas")
