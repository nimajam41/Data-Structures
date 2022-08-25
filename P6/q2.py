import math


class Node:
    def __init__(self, label):
        self.distance = 0
        self.label = label


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj = [[1000 for j in range(vertices)] for i in range(vertices)]
        self.nodes = [Node(i) for i in range(vertices)]

    def make_graph(self, a):
        if a[10] == 1:
            for i in range(self.vertices - 1):
                self.adj[i][i + 1] = 1
            self.adj[self.vertices - 1][0] = 1

        if a[11] == 1:
            for i in range(self.vertices - 1, 0, -1):
                self.adj[i][i - 1] = 1
            self.adj[0][self.vertices - 1] = 1

        for i in range(0, 10):
            if a[i] == 1:
                for x in range(self.vertices):
                    if x != i:
                        self.adj[x][i] = 1

        if a[12] == 1:
            for c in range(10, self.vertices):
                if a[c // 10] == 1 and a[c % 10] == 1:
                    for d in range(self.vertices):
                        if d != c:
                            self.adj[d][c] = min(self.adj[d][c], 3)

        for x in range(self.vertices):
            for y in range(self.vertices):
                if self.adj[x][y] == 1000:
                    self.adj[x][y] = 0

    def start(self, s):
        for node in self.nodes:
            node.distance = math.inf
        s.distance = 0

    def min_node(self, arr):
        m = math.inf
        u = None
        for node in self.nodes:
            if node.distance < m:
                if not arr[node.label]:
                    m = node.distance
                    u = node
        return u

    def dijkstra(self, src, dst):
        self.start(src)
        arr = [False for i in range(self.vertices)]
        for v in range(self.vertices):
            m = self.min_node(arr)
            if m is not None:
                arr[m.label] = True
                for node in self.nodes:
                    if self.adj[m.label][node.label] and not arr[node.label]:
                        if node.distance > m.distance + self.adj[m.label][node.label]:
                            node.distance = m.distance + self.adj[m.label][node.label]
        if dst.distance == math.inf:
            dst.distance = -1
        return dst.distance


graph = Graph(100)
v = [0] * 13
v[1], v[2], v[3], v[10] = map(int, input().split())
v[4], v[5], v[6], v[11] = map(int, input().split())
v[7], v[8], v[9] = map(int, input().split())
v[12], v[0] = map(int, input().split())
graph.make_graph(v)
x, y = map(int, input().split())
print(graph.dijkstra(graph.nodes[x], graph.nodes[y]))
