def in_order(a, b, index):
    n = len(a) - 1
    if index > n:
        return
    in_order(a, b, 2 * index + 1)
    b += [a[index]]
    in_order(a, b, 2 * index + 2)


def min_swap(a):
    b = [*enumerate(a)]
    b.sort(key=lambda iter: iter[1])
    done = [0] * len(a)
    result = 0
    for i in range(len(a)):
        if done[i] == 1 or b[i][0] == i:
            continue
        c = 0
        j = i
        while not done[j]:
            done[j] = 1
            j = b[j][0]
            c += 1
        if c != 0:
            result += c - 1
    return result


n = int(input())
a = [0] * n
li = input().split(" ")
for i in range(n):
    a[i] = int(li[i])
v = []
in_order(a, v, 0)
print(min_swap(v))
