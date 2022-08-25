from collections import defaultdict


class DAG:
    def __init__(self, vertices):
        self.g = defaultdict(list)
        self.vertices = vertices

    def add(self, a, b):
        self.g[a].append(b)

    def dfs(self, v, visited, start):
        visited[v] = True
        for i in self.g[v]:
            if not visited[i]:
                self.dfs(i, visited, start)
            else:
                start[v] = True

    def solve(self):
        start = [False for i in range(self.vertices)]
        visited = [False for i in range(self.vertices)]
        k = 1
        for i in range(self.vertices):
            if not visited[i]:
                self.dfs(i, visited, start)
            else:
                if start[i]:
                    for j in self.g[i]:
                        if visited[j] and i in self.g[j]:
                            k -= 1
                            if k < 0:
                                print("NO")
                                return
        print("YES")


n, k = map(int, input().split())
dag = DAG(n)
for i in range(k):
    a, b = map(int, input().split())
    dag.add(a - 1, b - 1)
dag.solve()
