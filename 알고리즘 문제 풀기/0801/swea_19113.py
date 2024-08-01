import sys

sys.stdin = open('txt/input_19113.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr_p = list(map(int, input().split()))
    answer = []
    for i in range(N * 2):
        if arr_p[i] != 0 and arr_p[i] % 3 == 0:
            answer.append(arr_p[i])
            for j in range(i + 1, N * 2):
                if arr_p[j] == int(arr_p[i] / 3) * 4:
                    arr_p[j] = 0
                    break  # 하나만 지우기 위해 break 문 사용
    print(f'#{tc}', end=' ')
    print(*answer)
