import sys

sys.stdin = open('txt/input_ws5.txt', 'r')


def rotate_arr(arr, n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 열 순회에서 행을 역순으로 순회하면 90도 돌린 배열
            answer[i][j] = arr[n - 1 - j][i]
    return answer


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기 N
    my_arr = [input().split() for _ in range(N)]
    rotate_90 = rotate_arr(my_arr, N)
    rotate_180 = rotate_arr(rotate_90, N)
    rotate_270 = rotate_arr(rotate_180, N)
    print(f'#{tc}')
    for i in range(N):
        print(f'{"".join(rotate_90[i])} {"".join(rotate_180[i])} {"".join(rotate_270[i])}')
