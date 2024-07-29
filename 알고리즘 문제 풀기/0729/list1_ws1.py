T = int(input())  # 테스트 케이스의 수
for t in range(1, T+1):
    N = int(input())  # 양수 N
    A = list(map(int, input().split()))  # N개의 요소를 가진 배열 A
    max_v = A[0]
    min_v = A[0]
    for i in A:
        if i > max_v:  # 최대값 비교
            max_v = i
        if i < min_v:  # 최소값 비교
            min_v = i
    print(f'#{t} {max_v - min_v}')
