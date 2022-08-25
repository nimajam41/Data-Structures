string = input()
goods_and_bads = input()
k = int(input())

l = len(string)
mod = 10 ** 18
arr = []
for i in range(l):
    res = 0
    count = 0
    j = 0
    while (i + j) < l:
        res = res * 31 + (ord(string[i + j]) - 96)
        res = res % mod
        if goods_and_bads[ord(string[i + j]) - 97] == '0':
            count += 1
        if k < count:
            break
        arr += [res]
        j += 1
arr.sort()
if len(arr) == 0:
    print(0)
else:
    answer = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer += 1
    print(answer)
