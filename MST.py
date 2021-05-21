import heapq

class DisJSet:
    # disjoint set data structure
    # mostly taken from canvas exercise
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        else:
            self.parent[yset] = xset
            self.rank[xset] += 1


def kruskal(G):
    # accepts graph in the form of an adjacency matrix and returns the matrix of the corresponding MST
    num = len(G)
    edges = []
    # iterate every element in the matrix, appending each edge to the edges list in the form of a tuple
    for i in range(num):
        # start iterating row at i+1 to avoid duplicates
        for j in range(i + 1, num):
            if G[i][j]:
                # tuple containing the two vertices and the edge weight
                edges.append((i, j, G[i][j]))

    # sort the edges by weight
    edges.sort(key=lambda edge: edge[2])

    # use disjoint set to check for cycles and MST list to hold MST edges
    ds = DisJSet(num)
    MST = []
    index = 0
    # MST should have V-1 edges, so keep looping until it reaches that size
    while len(MST) < num - 1:
        (v1, v2, w) = edges[index]
        index += 1
        # check if current edge would create a cycle and if not, append to MST
        x = ds.find(v1)
        y = ds.find(v2)
        if x != y:
            MST.append((v1,v2, w))
            ds.union(x,y)

    # just so the output matches the input- convert the MST back to an adjacency matrix.  Could also just
    # return MST here for a list of tuples corresponding to the MST edges.
    result = [[0 for i in range(num)] for j in range(num)]
    for edge in MST:
        (i,j,w) = edge
        result[i][j] = w
        result[j][i] = w
    return result


def prims(G):
    V = len(G)
    source = 0
    MST = []
    visited = [0]
    q = []
    for j in range(V):
        if G[0][j]:
            heapq.heappush(q, (G[0][j], 0, j))
    while len(visited) < V:
        next_edge = heapq.heappop(q)        # tuple: (weight, source, destination)
        next_v = next_edge[2]               # next vertex to be added if not already visited: destination from ^
        # if the vertex is already marked visited, move on
        if next_v in visited:
            continue
        # mark vertex as visited and add the edge to MST
        visited.append(next_v)
        MST.append(next_edge)
        # iterate through the current vertex's edges and add any that connect to
        # unvisited vertices to the queue
        for i in range(V):
            if G[next_v][i] and i not in visited:
                heapq.heappush(q, (G[next_v][i], next_v, i))
    # same as kruskal- could return MST here, but to make the output match the input format convert to matrix
    result = [[0 for i in range(V)] for j in range(V)]
    for edge in MST:
        w,i,j = edge
        result[i][j] = w
        result[j][i] = w
    return result



g1 = [[0, 9, 75, 0, 0],
      [9, 0, 95, 19, 42],
      [75, 95, 0, 51, 66],
      [0, 19, 51, 0, 31],
      [0, 42, 66, 31, 0]]
print(kruskal(g1))
print(prims(g1))