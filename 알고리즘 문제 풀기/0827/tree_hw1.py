import sys

sys.stdin = open("txt/in_hw1.txt", "r")


def in_order(t):
    global answer
    if t:  # 중위 순회
        in_order(lc[t])
        answer += arr[t]
        in_order(rc[t])


for tc in range(1, 11):
    N = int(input())  # 노드의 수 N
    arr = [" "] * (N + 1)  # 각 노드에 들어간 알파벳
    lc = [0] * (N + 1)  # 왼쪽 자식 노드 확인
    rc = [0] * (N + 1)  # 오른쪽 자식 노드 확인
    # 입력 받은 값을 각자의 위치에 맞게 할당
    for _ in range(N):
        temp = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        arr[temp[0]] = temp[1]
        # 값이 있을 경우에만
        lc[temp[0]] = temp[2] if len(temp) >= 3 else 0
        rc[temp[0]] = temp[3] if len(temp) == 4 else 0
    answer = ""
    in_order(1)
    print(f"#{tc} {answer}")
