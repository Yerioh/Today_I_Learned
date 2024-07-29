# T = int(input())
# for t in range(1, T+1):
# N = int(input())
# arr1 = list(map(int, input().split()))
N = 9
arr1 = [7, 4, 2, 0, 0, 6, 0, 7, 0]
arr2 = [0 for _ in range(N)]
for i in range(N-1):
    cnt = 0
    if arr1[i]:
        for j in range(i+1, N):
            if arr1[i] > arr1[j]:
                cnt += 1
    arr2[i] = cnt
print(arr2)