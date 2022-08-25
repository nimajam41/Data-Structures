class Node:
    def __init__(self):
        self.mark = False
        self.edges = [None] * 26
        self.count = 0
        self.result = None
        self.string_till_this_point = ""


def end_max(node):
    if node is None:
        return 0
    if node.result:
        return node.result
    else:
        result = (node.string_till_this_point, node.count)
        for edge in node.edges:
            if edge:
                m = end_max(edge)
                if m[1] > result[1]:
                    result = m
        node.result = result
        return result


def trie_insert(node, string, idx=0):
    if idx == len(string):
        node.mark = True
        node.count += 1
        return
    i = ord(string[idx]) - ord('a')
    if node.edges[i] is None:
        node.edges[i] = Node()
        node.edges[i].string_till_this_point = node.string_till_this_point + string[idx]
    trie_insert(node.edges[i], string, idx + 1)


def trie_find_prefix(node, string, idx):
    if idx == len(string):
        print(end_max(node)[0])
        print(end_max(node)[1])
        return
    else:
        i = ord(string[idx]) - ord('a')
        edge = node.edges[i]
        if edge is None:
            print(-1)
            return
        else:
            return trie_find_prefix(edge, string, idx + 1)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        trie_insert(self.root, string, idx=0)

    def find_prefix(self, string):
        trie_find_prefix(self.root, string, idx=0)


n = int(input())
s = list()
for i in range(n):
    s += [input()]
t = Trie()
for x in s:
    t.insert(x)
m = int(input())
query = list()
for j in range(m):
    query += [input()]
for q in query:
    t.find_prefix(q)
