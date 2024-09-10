import sys

sys.stdin = open("txt/in_hw.txt", "r")


def find_set(x):  # find_set 으로 무리의 대표자 선정
    if r[x] != x:
        r[x] = find_set(r[x])
    return r[x]


def union_set(x, y):  # 두 무리 합치기
    # 각 무리의 대표자
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:  # 대표자가 다를 경우에만
        if rank[root_x] > rank[root_y]:
            r[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            r[root_x] = root_y
        else:
            r[root_y] = root_x
            rank[root_x] += 1


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 마을 사람의 수, 관계의 수
    r = [i for i in range(N + 1)]
    rank = [1] * (N + 1)
    for _ in range(M):
        p1, p2 = map(int, input().split())  # 알고 있는 두 사람
        # 번호가 작은 쪽을 앞으로
        if p1 < p2:
            union_set(p1, p2)
        else:
            union_set(p2, p1)
    answer = 0
    for i in range(1, N + 1):  # 0 인덱스는 수를 맞추기 위한것 => 계산 X
        if r[i] == i:
            answer += 1
    print(f"#{tc} {answer}")
