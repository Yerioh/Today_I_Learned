N = 5
f = ["A", "B", "C", "D", "E"]
result = 0

for i in range(1 << N):
    cnt = 0
    for j in range(N):
        if i & (1 << j):
            cnt += 1
            print(j, end=" ")
    print()
    if cnt >= 2:
        result += 1
print(result)
