class Node:
    def __init__(self):
        self.online = True
        self.label = None
        self.neighbours = []


def just_one_max(node):
    global result
    if not node.online:
        return
    node.online = False
    if node.label > result:
        result = node.label
    for x in node.neighbours:
        if x.online:
            x.label += 1
            for y in x.neighbours:
                if y.online:
                    y.label += 1
    for x in node.neighbours:
        just_one_max(x)


def wanted(vertices, maximums, node):
    if len(maximums) == 1:
        just_one_max(node)
        global result
        print(result)
        quit()
    elif len(maximums) == 2:
        m1 = maximums[0]
        m2 = maximums[1]
        if m1 in m2.neighbours:
            print(node.label + 1)
            quit()
        for vertex in vertices:
            if vertex in m1.neighbours and vertex in m2.neighbours:
                print(node.label + 1)
                quit()
        print(node.label + 2)
        quit()
    elif len(maximums) > 2:
        for vertex in vertices:
            common = True
            for max_node in maximums:
                if not max_node == vertex and max_node not in vertex.neighbours:
                    common = False
                    break
            if common:
                print(node.label + 1)
                quit()
        print(node.label + 2)
        quit()


n = int(input())
vertices = [Node() for i in range(n)]
a = [*map(int, input().split())]
maximums = []
m_node = None
for i in range(n):
    vertices[i].label = a[i]
    if not m_node:
        maximums = [vertices[i]]
        m_node = vertices[i]
    elif vertices[i].label > m_node.label:
        maximums = [vertices[i]]
        m_node = vertices[i]
    elif vertices[i].label == m_node.label:
        maximums += [vertices[i]]

for i in range(n - 1):
    x = int(input())
    vertices[x - 1].neighbours += [vertices[i + 1]]
    vertices[i + 1].neighbours += [vertices[x - 1]]
result = m_node.label
wanted(vertices, maximums, m_node)
