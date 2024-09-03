arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
answer = 0
for i in range(1, 1 << N):
    sub = []
    for j in range(N):
        if i & (1 << j):
            sub.append(arr[j])
    if not sum(sub):
        answer += 1
        print(f"#{answer} {sub}")
