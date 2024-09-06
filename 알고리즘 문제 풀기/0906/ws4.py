import sys

sys.stdin = open("txt/in_ws4.txt", "r")

# 장훈이의 높은 선반

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, B = map(int, input().split())  # 점원의 수, 선반의 높이
    H = list(map(int, input().split()))  # 각 점원의 높이 수
    answer = sum(H)  # 선반 높이 이상 중 최소 합
    for i in range(1, 1 << N):
        s = 0  # 선택된 점원들의 높이 합
        for j in range(N):
            if i & (1 << j):
                s += H[j]
            if s > answer:
                break
        if B <= s < answer:
            answer = s
    print(f"#{tc} {answer - B}")
