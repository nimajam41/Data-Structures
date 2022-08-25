n = int(input())
li = input().split()
a = []
for i in range(len(li)):
    a += [int(li[i]) % 2]
stack = []
for x in a:
    if len(stack) == 0:
        stack.append(x)
    else:
        if x == stack[len(stack) - 1]:
            stack.pop()
        else:
            stack.append(x)
covered = 1
if len(stack) != 0:
    m = stack[0]
    for i in range(1, len(stack), 1):
        if stack[i] != m:
            covered = 0
            break
if covered == 1:
    print("YES")
else:
    print("NO")
