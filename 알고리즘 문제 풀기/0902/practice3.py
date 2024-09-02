# 중복순열 [1, 1, 1] ~ [6, 6, 6] 까지 출력하는 코드를 재귀호출로 구현하자.
def permutation1(v):
    if v == N:
        print(*result)
        return
    for i in range(M):
        result[v] = i + 1
        permutation1(v + 1)


# 중복을 허용하지 않는 순열 출력
def permutation2(v):
    if v == N:
        print(*result)
        return
    for i in range(M):
        if not used[i]:
            result[v] = i + 1
            used[i] = 1
            permutation2(v + 1)
            used[i] = 0


N, M = map(int, input().split())
result = [0] * N
used = [0] * M
print("중복을 허용하는 순열")
permutation1(0)
print("---------------------")
print("중복을 허용하지 않는 순열")
permutation2(0)
