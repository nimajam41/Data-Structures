class Node:
    def __init__(self, start, right, index):
        self.parent = self
        self.start = start
        self.right = right
        self.rank = 0
        self.index = index


class DSU:
    def __init__(self, n, starts, ends):
        self.n = n
        self.nodes = [Node(starts[i], starts[i] + ends[i], n - 1 - i) for i in range(self.n)]

    def find(self, u):
        if u == u.parent:
            return u
        u.parent = self.find(u.parent)
        return u.parent

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return False
        if u.rank > v.rank:
            u, v = v, u
        u.parent = v
        if u.rank == v.rank:
            v.rank += 1

        v.right = max(v.right, u.right)
        v.start = min(v.start, u.start)
        v.index = min(v.index, u.index)
        return True

    def size(self):
        c = 0
        for node in self.nodes:
            if node.parent == node:
                c += 1
        return c


n = int(input())
x = []
h = []
for i in range(n):
    li = input().split(" ")
    x += [int(li[0])]
    h += [int(li[1])]
dsu = DSU(n, x, h)
maximum_falls_index = [n - 1]
result_stack = []
rights = [0] * n
rights[n - 1] = x[n - 1] + h[n - 1]
q = int(input())
queries = []
answers = [0] * q
for j in range(q):
    li = input().split(" ")
    l = int(li[0]) - 1
    r = int(li[1]) - 1
    queries += [(l, r, j)]

queries.sort(key=lambda y: (y[0], y[1]), reverse=True)
state = n - 1
for query in queries:
    l = query[0]
    r = query[1]
    index = query[2]

    if state > l:
        for t in range(state - 1, l - 1, -1):
            fall = x[t] + h[t]
            while True:
                if len(maximum_falls_index) == 0 or x[maximum_falls_index[-1]] > fall:
                    rights[t] = fall
                    if len(maximum_falls_index) > 0:
                        gap = 0
                        if len(result_stack) > 0:
                            gap = result_stack[-1]
                        result_stack += [gap + x[maximum_falls_index[-1]] - fall]
                    maximum_falls_index += [t]
                    v = dsu.find(dsu.nodes[t])
                    v.index = len(maximum_falls_index) - 1
                    break

                if x[maximum_falls_index[-1]] <= fall:
                    u = maximum_falls_index.pop()
                    if len(result_stack) > 0:
                        result_stack.pop()
                    fall = max(fall, rights[u])
                    dsu.union(dsu.nodes[t], dsu.nodes[u])

        state = l

    if dsu.find(dsu.nodes[l]) == dsu.find(dsu.nodes[r]):
        answers[index] = 0
    else:
        idx1 = dsu.find(dsu.nodes[l]).index
        idx2 = dsu.find(dsu.nodes[r]).index
        b = 0
        if idx2 > 0:
            b = result_stack[idx2 - 1]
        a = result_stack[idx1 - 1]
        answers[index] = a - b

for ans in answers:
    print(ans)
