a = input()
str = ""
for x in range(len(a) - 2):
    str += (a[x] + '2')
str += (a[len(a) - 2])
result = 1
left = [0] * len(str)
right = [0] * len(str)
left[0] = int(str[0])
right[len(str) - 1] = int(str[len(str) - 1])
for i in range(1, len(str)):
    left[i] = (left[i - 1] * 3 + int(str[i])) % (10 ** 9 + 7)
for i in range(len(str) - 2, -1, -1):
    right[i] = (right[i + 1] * 3 + int(str[i])) % (10 ** 9 + 7)
mod = 10 ** 9 + 7
powers = [0] * 100001
powers[0] = 1
for i in range(1, 100001):
    powers[i] = powers[i - 1] * 3 % (10 ** 9 + 7)
length = len(str)


def is_palindrome(center, l):
    le = center - l
    ri = center + l
    hl = left[ri]
    if le > 0:
        hl = hl - (left[le - 1] * powers[ri - le + 1])
    hl %= mod
    hr = right[le]
    if ri < length - 1:
        hr = hr - (right[ri + 1] * powers[ri - le + 1])
    hr %= mod
    return hr == hl


result = 0
for x in range(len(str)):
    start = 0
    end = min(abs(x - 0), abs(x - (len(str) - 1)))
    if is_palindrome(x, end):
        res = 2 * end + 1
    else:
        while end > start + 1:
            mid = (start + end) // 2
            if is_palindrome(x, mid):
                start = mid
            else:
                end = mid
        if str[start] != '2':
            res = 2 * start + 1
        else:
            res = 2 * start - 1
    result = max(result, res)
print((result+1) // 2)
