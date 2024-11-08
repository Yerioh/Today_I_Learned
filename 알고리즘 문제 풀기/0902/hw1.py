import sys

sys.stdin = open("txt/in_hw1.txt", "r")


def exchange(v, idx):  # 현재 교환 횟수, 현재 자리
    global answer
    if v == N:  # 교환 횟수를 채웠다면
        num = int("".join(num_board))
        if num > answer:
            answer = num
        return
    if idx == n:  # 자리가 범위를 넘어간다면 뒤 두 자리만 반복하여 교환
        num_board[n - 1], num_board[n - 2] = num_board[n - 2], num_board[n - 1]
        exchange(v + 1, idx)
        num_board[n - 1], num_board[n - 2] = num_board[n - 2], num_board[n - 1]
    else:
        for i in range(n):
            if idx == i:  # 현재 자리와 교환할 자리가 같으면 교환하지 않는 것
                exchange(v, idx + 1)
            else:  # 다르면서 해당 위치가 교환이 가능하다면
                num_board[idx], num_board[i] = num_board[i], num_board[idx]
                exchange(v + 1, idx + 1)
                num_board[idx], num_board[i] = num_board[i], num_board[idx]


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = input().split()
    num_board, N = list(arr[0]), int(arr[1])  # 보드판의 정보, 교환 횟수
    n = len(num_board)  # 숫자판의 개수
    answer = 0
    unused = [0] * n
    exchange(0, 0)
    print(f"#{tc} {answer}")