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

    def union(self,x,y):
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
            self.rank[xset] = self.rank[xset] + 1


def kruskal(G):
    num = len(G)
    edges = []
    for i in range(num):
        for j in range(i+1, num):
            if G[i][j]:
                edges.append(((i,j), G[i][j]))

    sorted_edges = []
    for edge in sorted(edges, key=lambda edge: edge[1]):
        sorted_edges.append(edge)
    return sorted_edges

    # MST = {}
    # index = 0
    # while len(MST) < num-1:
    #     (v1, v2) = sorted_edges[index]
    #
    # ds = DisJSet(num)




g1 =  [[0, 9, 75, 0, 0],
 [9, 0, 95, 19, 42],
 [75, 95, 0, 51, 66],
 [0, 19, 51, 0, 31],
 [0, 42, 66, 31, 0]]
print(kruskal(g1))