import sys

sys.stdin = open("txt/in_hw1.txt", "r")


def exchange(v):  # 현재 교환 횟수
    global answer
    if v == N:  # 교환 횟수를 채웠다면
        num = int("".join(num_board))
        if num > answer:
            answer = num
        return
    # 교환 위치 조합
    for i in range(n):
        for j in range(i + 1, n):
            num_board[i], num_board[j] = num_board[j], num_board[i]  # 교환
            temp_num = int("".join(num_board))
            if temp_num not in num_lists[v]:  # 교환해서 나왔던적이 있는 숫자인지 확인
                num_lists[v].append(temp_num)
                exchange(v + 1)
            num_board[i], num_board[j] = num_board[j], num_board[i]  # 교환 초기화


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = input().split()
    num_board, N = list(arr[0]), int(arr[1])  # 보드판의 정보, 교환 횟수
    n = len(num_board)  # 숫자판의 개수
    answer = 0
    num_lists = [[] for _ in range(N)]
    exchange(0)
    print(f"#{tc} {answer}")
