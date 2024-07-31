import sys

sys.stdin = open('in.txt', 'r')


# 대각선의 합
def cross_sum1(arr, n):
    s = 0
    # for 문 한번
    for i in range(n):
        s += arr[i][i] + arr[i][-1 - i]
    s -= arr[n // 2][n // 2] if n % 2 else 0
    return s


def cross_sum2(arr, n):
    s = 0
    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                s += arr[i][j]
    return s


# 인접 요소와의 절대값의 총합
def delta_abs_sum(arr, n):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total = 0
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n:
                    s += abs(arr[i][j] - arr[ni][nj])
            total += s
    return total


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    my_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t}')
    print(f'대각선의 합1 : {cross_sum1(my_arr, N)}')
    print(f'대각선의 합2 : {cross_sum2(my_arr, N)}')
    print(f'인접 요소와의 차의 절대값의 총합 : {delta_abs_sum(my_arr, N)}')
