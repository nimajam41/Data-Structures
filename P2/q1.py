def inversion(A, B):
    if len(A) > 1:
        res = 0
        mid = len(A) // 2
        LA = A[:mid]
        RA = A[mid:]
        LB = B[:mid]
        RB = B[mid:]

        s1 = inversion(LA, LB)
        s2 = inversion(RA, RB)

        i = j = k = 0

        while i < len(LA) and j < len(RA):
            if LA[i] < RA[j]:
                A[k] = LA[i]
                i += 1
            else:
                A[k] = RA[j]
                j += 1
            k += 1

        while i < len(LA):
            A[k] = LA[i]
            i += 1
            k += 1

        while j < len(RA):
            A[k] = RA[j]
            j += 1
            k += 1

        i = j = k = 0

        while i < len(LB) and j < len(RB):
            if LB[i] < RB[j]:
                B[k] = LB[i]
                i += 1
            else:
                B[k] = RB[j]
                j += 1
            k += 1

        while i < len(LB):
            B[k] = LB[i]
            i += 1
            k += 1

        while j < len(RB):
            B[k] = RB[j]
            j += 1
            k += 1

        i = j = 0
        RB += [100000000]
        while i < len(LA):
            while LA[i] > RB[j]:
                j += 1
            res += j
            i += 1

        return s1 + s2 + res

    else:
        return 0


n = int(input())
li = input().split(" ")
a = []
counter = [0] * (n + 1)
counter_from_first = [0] * n
for i in range(len(li)):
    a += [int(li[i])]
    counter[a[i]] += 1
    counter_from_first[i] = counter[a[i]]
counter_from_last = [0] * n
for i in range(len(a)):
    counter_from_last[i] = counter[a[i]] + 1 - counter_from_first[i]
print(inversion(counter_from_first, counter_from_last))
