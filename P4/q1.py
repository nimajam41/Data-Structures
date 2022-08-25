import math


class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def size(self):
        return len(self.heap)

    def bubble_down(self, index):
        while (2 * index) < self.size():
            temp = index
            if self.heap[2 * index] > self.heap[index]:
                temp = 2 * index
            if 2 * index + 1 < self.size():
                if self.heap[2 * index + 1] > self.heap[temp]:
                    temp = 2 * index + 1
            if temp == index:
                break
            self.heap[temp], self.heap[index] = self.heap[index], self.heap[temp]
            index = temp

    def bubble_up(self, index):
        while index > 1 and self.heap[index] > self.heap[index // 2]:
            self.heap[index // 2], self.heap[index] = self.heap[index], self.heap[index // 2]
            index = index // 2

    def insert(self, obj):
        self.heap += [obj]
        self.bubble_up(self.size() - 1)

    def get_max(self):
        return self.heap[1]

    def del_max(self):
        self.heap[1] = self.heap[-1]
        del (self.heap[-1])
        self.bubble_down(1)

    def build_by_bubble_down(self, a):
        self.heap = [0] + a
        for i in range(len(a) + 1, 0, -1):
            self.bubble_down(i)


class MinHeap:
    def __init__(self):
        self.heap = [0]

    def size(self):
        return len(self.heap)

    def bubble_down(self, index):
        while (2 * index) < self.size():
            temp = index
            if self.heap[2 * index] < self.heap[index]:
                temp = 2 * index
            if 2 * index + 1 < self.size():
                if self.heap[2 * index + 1] < self.heap[temp]:
                    temp = 2 * index + 1
            if temp == index:
                break
            self.heap[temp], self.heap[index] = self.heap[index], self.heap[temp]
            index = temp

    def bubble_up(self, index):
        while index > 1 and self.heap[index] < self.heap[index // 2]:
            self.heap[index // 2], self.heap[index] = self.heap[index], self.heap[index // 2]
            index = index // 2

    def insert(self, obj):
        self.heap += [obj]
        self.bubble_up(self.size() - 1)

    def get_min(self):
        return self.heap[1]

    def del_min(self):
        self.heap[1] = self.heap[-1]
        del (self.heap[-1])
        self.bubble_down(1)

    def build_by_bubble_down(self, a):
        self.heap = [0] + a
        for i in range(len(a) + 1, 0, -1):
            self.bubble_down(i)


b = [*map(int, input().split())]
n = b[0]
k = b[1]
res = 0
minHeap = MinHeap()
maxHeap = MaxHeap()
a = [*map(int, input().split())]
minHeap.build_by_bubble_down(a)
maxHeap.build_by_bubble_down(a)
for i in range(k):
    maximum = maxHeap.get_max()
    minimum = minHeap.get_min()
    minHeap.del_min()
    maxHeap.del_max()
    t = math.floor((maximum + minimum) / 2)
    u = math.ceil((maximum + minimum) / 2)
    maxHeap.insert(t)
    maxHeap.insert(u)
    minHeap.insert(t)
    minHeap.insert(u)
    res += (maximum - t) + (u - minimum)
print(int(res))
