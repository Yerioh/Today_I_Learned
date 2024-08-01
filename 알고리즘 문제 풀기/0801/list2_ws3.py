import sys

sys.stdin = open('txt/input_ws3.txt', 'r')

# sort(), min(), max() 사용 금지

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 정수의 개수
    arr = list(map(int, input().split()))  # N개 숫자들의 배열
    answer = [0] * N  # 정렬된 배열
    for i in range(N):
        # 인덱스가 짝수라면 큰 값 찾기
        if not i % 2:
            max_idx = 0
            max_num = 0
            for j in range(len(arr)):
                if 1 <= arr[j] <= 100 and arr[j] > max_num:
                    max_idx = j
                    max_num = arr[j]
            answer[i] = arr[max_idx]
            arr[max_idx] = 0
        # 인덱스가 홀수라면 작은 값 찾기
        else:
            min_idx = 0
            min_num = 101
            for j in range(len(arr)):
                if 1 <= arr[j] <= 100 and arr[j] < min_num:
                    min_idx = j
                    min_num = arr[j]
            answer[i] = arr[min_idx]
            arr[min_idx] = 0
    print(f'#{tc}', end=' ')
    print(*answer[:10])
