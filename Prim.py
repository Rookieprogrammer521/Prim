def weight(A, u, v):
    return A[u][v]


def adjacent(A, u):
    L = []
    for x in range(len(A)):
        if A[u][x] > 0 and x <> u:
            L.insert(0,x)
    return L


def extractMin(Q):
    q = Q[0]
    Q.remove(Q[0])
    return q


def decreaseKey(Q, K):
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] < K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s


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
