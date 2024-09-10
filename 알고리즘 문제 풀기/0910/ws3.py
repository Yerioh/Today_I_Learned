import sys

sys.stdin = open("txt/in_ws3.txt", "r")


def bfs(q):
    temp = []
    idx = 0
    # 앞 회차에서 연락 받은 사람들이 연락을 돌릴 차례
    while idx < len(q):
        p = q[idx]
        idx += 1
        for c in adj_l[p]:
            if not v[c]:
                v[c] = v[p] + 1
                temp.append(c)
    if not temp:  # temp가 비었다면 연락이 종료
        return max(q)  # q 중 최댓값이 답
    return bfs(temp)


for tc in range(1, 11):
    N, S = map(int, input().split())  # 데이터의 길이, 연락 시작점
    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(101)]  # 100번까지의 인접리스트
    for i in range(0, N, 2):
        x, y = arr[i], arr[i + 1]
        if y not in adj_l[x]:
            adj_l[x].append(y)
    # 큐 초기 설정
    v = [0] * 101
    v[S] = 1
    answer = bfs([S])
    print(f"#{tc} {answer}")
