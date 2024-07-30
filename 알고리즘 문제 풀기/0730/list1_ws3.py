T = int(input())  # 테스트 케이스의 수
for t in range(1, T+1):
    N = int(input())  # 수열의 길이 N
    arr = list(map(int, input()))  # 수열을 담은 배열
    max_cnt = 0  # 연속된 1의 개수 중 가장 큰 값
    for i in range(N):
        cnt = 0
        if arr[i]:  # 현 위치의 값이 1이라면
            for j in range(i, N):
                if not arr[j]:  # 0이 검출된다면
                    break
                else:
                    cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    print(f'#{t} {max_cnt}')
