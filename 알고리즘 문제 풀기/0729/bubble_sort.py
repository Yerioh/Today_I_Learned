N = 5
a = [55, 7, 78, 12, 42]

for i in range(N):  # for i in range(N-1, 0, -1)
    for j in range(N-i-1):  # for j in range(0, i)
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(*a)
