line = input()
n = int(line)
start = [0] * 1001
end = [0] * 1001
for i in range(n):
    line = input()
    li = line.split(' ')
    a = int(li[0])
    b = int(li[1])
    start[a] += 1
    end[b] += 1
sumStart = [start[0]]
sumEnd = [end[0]]
length = 1
counter = [start[0]]
for i in range(1, 1001, 1):
    sumStart += [sumStart[length - 1] + start[length]]
    sumEnd += [sumEnd[length - 1] + end[length]]
    counter += [sumStart[length] - sumEnd[length - 1]]
    length += 1
finalCount = [0] * n
for x in counter:
    if x in range(1, n + 1, 1):
        finalCount[x - 1] += 1
for i in range(len(finalCount)):
    if i == len(finalCount) - 1:
        print(finalCount[i], end='')
    else:
        print(finalCount[i])
