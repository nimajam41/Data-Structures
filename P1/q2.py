line = input()
n = int(line)
count = [0] * 1001
for i in range(n):
    line = input()
    li = line.split(' ')
    a = int(li[0])
    b = int(li[1])
    for x in range(a, b + 1, 1):
        count[x] += 1
counter = [0] * n
for x in count:
    if x in range(1, n + 1, 1):
        counter[x - 1] += 1
for i in range(len(counter)):
    if i == len(counter) - 1:
        print(counter[i], end='')
    else:
        print(counter[i])
