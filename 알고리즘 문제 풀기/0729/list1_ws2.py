T = int(input()) # 테스트 케이스의 수
for t in range(1, T+1):
    N, M = map(int, input().split())  # 배열의 크기 N, 합할 구간의 크기 M
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = 0
    for i in range(N-M+1):
        num_sum = 0
        for j in range(M):  # M만큼 반복하여 구간의 크기 구하기
            num_sum += arr[i+j]
        if i == 0:  # 첫 반복이라면
            max_sum = num_sum
            min_sum = num_sum
        else:
            if num_sum > max_sum:  # 최대값 비교
                max_sum = num_sum
            if num_sum < min_sum:  # 최소값 비교
                min_sum = num_sum
    print(f'#{t} {max_sum - min_sum}')