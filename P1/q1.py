line = input()
li = line.split(' ')
n = int(li[0])
q = int(li[1])
sums = [0]
prints = []
offsets = [0] * n
for i in range(q):
    line = input()
    li = line.split(' ')
    if li[0] == "IN":
        num = int(li[1])
        if len(sums) != 0:
            lastIndex = len(sums) - 1
            sums += [sums[lastIndex] + num]
    else:
        row = int(li[1]) - 1
        j = int(li[2])
        temp = offsets[row]
        offsets[row] += j
        result = sums[offsets[row]] - sums[temp]
        prints += [result]
for x in range(len(prints)):
    if x == len(prints) - 1:
        print(prints[x], end='')
    else:
        print(prints[x])
