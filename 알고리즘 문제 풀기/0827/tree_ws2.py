import sys

sys.stdin = open("txt/in_ws2.txt", "r")


def pre_order(t):  # 루트 노드부터 전위 순회하여 카운트
    global answer
    if t:
        answer += 1
        pre_order(lc[t])
        pre_order(rc[t])


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # 간선의 개수 E, 루트 노드 N
    # 리스트로 노드 관계 나타내기
    arr = list(map(int, input().split()))
    lc = [0] * (E + 2)
    rc = [0] * (E + 2)
    par = [0] * (E + 2)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if lc[p] == 0:
            lc[p] = c
        else:
            rc[p] = c
        par[c] = p
    answer = 0
    pre_order(N)
    print(f"#{tc} {answer}")
