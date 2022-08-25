import math


class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0


class DSU:
    def __init__(self, n):
        self.n = n
        self.nodes = [Node() for x in range(n)]

    def find(self, u):
        if u == u.parent:
            return u
        u.parent = self.find(u.parent)
        return u.parent

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        self.n -= 1
        if u.rank > v.rank:
            u, v = v, u
        u.parent = v
        if u.rank == v.rank:
            v.rank += 1
        return

    def needed_power(self):
        return self.n // 2 - 1


n, m = map(int, input().split())
dsu = DSU(2 * n)
res = 100
for i in range(m):
    a, b, c = map(int, input().split())
    x = 2 * a - 2
    y = 2 * b - 2
    if c == 1:
        if dsu.find(dsu.nodes[x]) == dsu.find(dsu.nodes[y + 1]):
            res = 0
        else:
            dsu.union(dsu.nodes[x], dsu.nodes[y])
            dsu.union(dsu.nodes[x + 1], dsu.nodes[y + 1])
    else:
        if dsu.find(dsu.nodes[x]) == dsu.find(dsu.nodes[y]):
            res = 0
        else:
            dsu.union(dsu.nodes[x], dsu.nodes[y + 1])
            dsu.union(dsu.nodes[x + 1], dsu.nodes[y])
if res == 0:
    print(res)
else:
    print(pow(2, dsu.needed_power()) % 1000000007)
