def search(array, k):
    start = 0
    end = len(array)

    while end > start + 1:
        mid = (start + end) // 2

        if array[mid] >= k:
            end = mid

        else:
            start = mid

    return start


n, q = map(int, input().split())
arr = []
sums = [0]
for i in range(n):
    l, r = map(int, input().split())
    arr += [(l, r)]

arr.sort(key=lambda y: y[0])

for i in range(n):
    l, r = arr[i]
    if i == 0:
        sums += [r - l + 1]
    else:
        sums += [sums[-1] + r - l + 1]

for j in range(q):
    query = int(input())
    s = search(sums, query)
    l, r = arr[s]
    t = query - sums[s]
    print(l + t - 1)
