class Graph:
    def __init__(self, v):
        self.edges = [[] for i in range(v)]
        self.parts = [0 for i in range(v)]
        self.marks = [0 for i in range(v)]
        self.size = 0

    def add_edge(self, v, u):
        self.edges[v - 1].append(u - 1)
        self.edges[u - 1].append(v - 1)

    def bfs_for_farthest(self, root):
        visited = [False for i in range(len(self.edges))]
        visited[root] = True
        q = [root]
        res = [root]
        while len(q) > 0:
            now = q.pop(0)
            for x in self.edges[now]:
                if visited[x] is False:
                    q.append(x)
                    visited[x] = True
                    res += [x]
        for i in range(len(res) - 1, -1, -1):
            if self.parts[res[i]] == 1:
                return res[i]

    def bfs_till(self, root, dist):
        heights = [-1 for i in range(len(self.parts))]
        visited = [False for i in range(len(self.edges))]
        visited[root] = True
        q = [root]
        heights[root] = 0
        if dist == 0:
            return
        while len(q) > 0:
            now = q.pop(0)
            if heights[now] > d:
                break
            self.marks[now] += 1
            for x in self.edges[now]:
                if visited[x] is False and heights[x] == -1:
                    q.append(x)
                    visited[x] = True
                    heights[x] = heights[now] + 1


n, m, d = map(int, input().split())
g = Graph(n)
li = [*map(int, input().split(" "))]
for x in li:
    g.parts[x - 1] = 1
for i in range(n - 1):
    a, b = map(int, input().split())
    g.add_edge(a, b)
x = g.bfs_for_farthest(li[0] - 1)
if m > 1:
    y = g.bfs_for_farthest(x)
else:
    y = None
g.bfs_till(x, d)
g.bfs_till(y, d)
c = 0
for x in g.marks:
    if x == 2:
        c += 1
print(c)
