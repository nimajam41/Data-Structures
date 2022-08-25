def gcd(a, b):
    m = min(a, b)
    if a % m == 0 and b % m == 0:
        return m
    for i in range(m // 2, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def divisors(n):
    A = []
    for x in range(1, n // 2 + 1, 1):
        if n % x == 0:
            A += [x]
    A += [n]
    return A


def hash_function(string):
    res = 0
    p = 31
    for i in range(len(string)):
        res = res * p + ord(string[i])
    return res


a = input()
b = input()
c = gcd(len(a), len(b))
m = max(len(a), len(b))

result = 0
if hash_function(a[0:1]) != hash_function(b[0:1]):
    print(0)
    exit()

else:
    if m == len(a):
        a, b = b, a
    arr = divisors(c)
    ans = []
    res = 0
    for x in arr:
        hashed = hash_function(b[0:x])
        start = 0
        last = x
        problem = False
        while last != len(a):
            if hash_function(a[start:last]) == hashed:
                start += x
                last += x
            else:
                problem = True
                break
        if problem:
            continue

        else:
            res += 1

    print(res)
