import sys

sys.stdin = open("txt/in_ws1.txt", "r")


def in_order(t):
    global cnt
    if t:
        # 중위 순회
        in_order(lc[t])
        cnt += 1  # 값을 넣기 전에 카운트
        answer[t] = cnt
        in_order(rc[t])


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())
    # 루트 노드를 1로 하는 완전 이진 트리 만들기
    lc = [0] * (N + 1)  # 왼쪽 자식 노드
    rc = [0] * (N + 1)  # 오른쪽 자식 노드
    for i in range(2, N + 1):
        if i % 2:
            rc[i//2] = i
        else:
            lc[i//2] = i
    answer = [0] * (N + 1)  # 중위 순회 하며 값을 넣을 리스트
    cnt = 0  # 넣어줄 값
    in_order(1)
    print(f"#{tc} {answer[1]} {answer[N//2]}")

# 인접 리스트로 완전 이진 트리 만들기
# T = int(input())  # 테스트 케이스의 수
# for tc in range(1, T + 1):
#     N = int(input())
#     # 인접 리스트의 형태로 각 노드 연결 만들기
#     num = 2
#     adj_l = [[]]
#     while num <= N:
#         temp = [0] * 2
#         for i in range(2):
#             if num <= N:
#                 temp[i] = num
#                 num += 1
#         adj_l.append(temp)
#     answer = [0] * (N + 1)  # 중위 순회 하며 값을 넣을 리스트
#     cnt = 0  # 넣어줄 값
#     in_order(1)
#     print(f"#{tc} {answer[1]} {answer[N//2]}")
