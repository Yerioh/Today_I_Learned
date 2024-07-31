import sys

sys.stdin = open('input_ws1.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 부분 집합의 원소 수 N, 원소의 합이 K인 부분 집합
    N, K = map(int, input().split())
    # 부분 집합 찾기
    count_subset = 0
    true_subset = []
    # 1 ~ 12 까지의 모든 부분 집합 찾기
    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(j + 1)
        # 부분집합의 길이가 N 이고 합이 K인 부분 집합만 검사
        if len(subset) == N and sum(subset) == K:
            count_subset += 1
            true_subset.append(subset)
    print(f'#{tc} {count_subset}')
