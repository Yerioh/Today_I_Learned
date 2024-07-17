# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 입력 받은 숫자의 리스트
    li = list(map(int, input().split()))
    # 숫자 합 초기화
    num_sum = 0
    # 숫자 더한 횟수 초기화
    count = 0
    for i in li:
        # 최대값 최소값과 다르다면 더하고 카운트업
        if i != max(li) and i != min(li):
            count += 1
            num_sum += i
    print(f'#{t} {round(num_sum/count)}')