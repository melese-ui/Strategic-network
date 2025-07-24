import numpy as np
import random as rand

# Example matrix for demonstration purposes
G = np.array([
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
])

# Degree of node a in network G
def degree(G, a):
    return sum(G[a])

# Power of the adjacency matrix (by recursion)
def power(G, k):
    if k == 0:
        return np.identity(len(G), dtype=int)
    elif k == -1:
        return G
    else:
        return G.dot(power(G, k - 1))

# Shortest path distance between node i and j in G (by using powers)
def distance(G, i, j):
    n = len(G)
    if i == j:
        return 0
    else:
        k = 1
        while k <= n - 1:
            if power(G, k)[i, j] > 0:
                return k
            k = k + 1
        return -1

# Benefit function
def benefit(s, k):
    return s**k

# Number of nodes in the network
def numberofnodes(G):
    return len(G)

# Create an empty network of size n
def create_Empty_Network(n):
    return np.array([[0]*n for _ in range(n)])

# Create a star network with n nodes and a given center
def create_Star_Network(n, center):
    G = [[0]*n for _ in range(n)]
    for i in range(n):
        if i != center:
            G[center][i] = 1
            G[i][center] = 1
    return np.array(G)

# Create a random undirected network with connection probability p
def random_network(n, p):
    L = create_Empty_Network(n)
    for i in range(n):
        for j in range(i + 1, n):
            r = rand.random()
            if r < p:
                L[i][j] = 1
                L[j][i] = 1
    return L

# Eccentricity of node a in G (maximum distance to any other node)
def eccentricity(G, a):
    n = len(G)
    max_dist = 0
    for i in range(n):
        d = distance(G, a, i)
        if i != a and d > max_dist:
            max_dist = d
    return max_dist

# Utility of node i in distance-based utility model
def utility(G, s, a, c):
    utility_value = 0
    n = numberofnodes(G)
    for i in range(n):
        k = distance(G, a, i)
        if k > 0:
            utility_value = utility_value + benefit(s, k)
    return utility_value - c * degree(G, a)

# Total utility of the network in the distance-based utility model
def totalutility(G, s, c):
    n = numberofnodes(G)
    sum_utility = 0
    for i in range(n):
        sum_utility += utility(G, s, i, c)
    return sum_utility

# Create a complete network of size n
def create_Complete_Network(n):
    G = [[1]*n for _ in range(n)]
    for i in range(n):
        G[i][i] = 0
    return np.array(G)
