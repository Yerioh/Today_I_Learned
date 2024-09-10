"""
8
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
4 3
1 2 2 4 3 4
3 2
1 2 2 1
5 3
1 2 3 4 4 5
5 3
5 4 4 3 2 1

1
15 9
1 4 2 5 6 2 7 3 8 9 11 3 12 14 14 9 15 1

"""


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(T):
    N, M = map(int, input().split())  # N명의 학생, M장의 신청서
    arr = list(map(int, input().split()))  # 신청서의 내용
    parent = [i for i in range(N + 1)]
    rank = [1] * (N + 1)
    for i in range(M):
        student1, student2 = arr[i * 2], arr[i * 2 + 1]
        if student1 > student2:
            union(student2, student1)
        else:
            union(student1, student2)
    result = 0  # 자기 자신이 부모인 것만 세자
    for i in range(1, N + 1):
        if i == parent[i]:
            result += 1
    answer[tc] = f"#{tc + 1} {result}"
print(*answer, sep="\n")
