def binary(n):
    s = ''
    k = 27
    while k != 0:
        i = n % 2
        n = n // 2
        k -= 1
        s += chr(i + 48)
    return st_reverse(s)


def st_reverse(s):
    t = ''
    for i in range(len(s)):
        t += s[len(s) - i - 1]
    return t


class Node:
    def __init__(self):
        self.edges = [None] * 2
        self.count = 0


def trie_insert(node, string, idx=0):
    if idx == len(string):
        return
    i = ord(string[idx]) - ord('0')
    if node.edges[i] is None:
        node.edges[i] = Node()
    node.edges[i].count += 1
    trie_insert(node.edges[i], string, idx + 1)


def trie_delete(node, string, idx):
    if idx == len(string):
        return
    i = ord(string[idx]) - ord('0')
    node.edges[i].count -= 1
    trie_delete(node.edges[i], string, idx + 1)


def trie_xor(node, s1, s2, idx):
    if idx == len(s1):
        return 0
    else:
        if s2[idx] == '0':
            i = abs(ord(s1[idx]) - ord('0'))
            edge = node.edges[i]
            if edge is None:
                return 0
            else:
                return trie_xor(edge, s1, s2, idx + 1)
        else:
            i = abs(ord(s1[idx]) - ord('0'))
            if node.edges[i] is None and node.edges[(i + 1) % 2] is None:
                return node.count
            if node.edges[i] is None and node.edges[(i + 1) % 2] is not None:
                return trie_xor(node.edges[(i + 1) % 2], s1, s2, idx + 1)
            if node.edges[i] is not None and node.edges[(i + 1) % 2] is None:
                return node.edges[i].count
            if node.edges[i] is not None and node.edges[(i + 1) % 2] is not None:
                return node.edges[i].count + trie_xor(node.edges[(i + 1) % 2], s1, s2, idx + 1)


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        trie_insert(self.root, string, idx=0)

    def delete(self, string):
        trie_delete(self.root, string, idx=0)

    def army(self, s1, s2):
        return trie_xor(self.root, s1, s2, idx=0)


q = int(input())
trie = Trie()
for i in range(q):
    li = input().split(" ")
    if int(li[0]) == 1:
        s = binary(int(li[1]))
        trie.insert(s)
    if int(li[0]) == 2:
        s = binary(int(li[1]))
        trie.delete(s)
    if int(li[0]) == 3:
        p = int(li[1])
        l = int(li[2])
        s1 = binary(p)
        s2 = binary(l)
        m = trie.army(s1, s2)
        print(m)
