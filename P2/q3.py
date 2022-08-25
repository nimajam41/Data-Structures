n = int(input())
line = input().split()
a = [0] * n
for i in range(n):
    a[i] = int(line[i])
maxXOR = 0
for i in range(n - 1):
    c = a[i] ^ a[i + 1]
    if c > maxXOR:
        maxXOR = c
max2 = 0
for i in range(n - 2):
    if max(a[i:i + 3]) == a[i + 1]:
        c = a[i] ^ a[i + 2]
        if c > max2:
            max2 = c
if max2 > maxXOR:
    print(max2)
else:
    print(maxXOR)
