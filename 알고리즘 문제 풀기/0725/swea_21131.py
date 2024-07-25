import sys
sys.stdin = open("input_21131.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    N = int(input()) # 행렬의 크기 N
    A = [list(map(int, input().split())) for _ in range(N)] # 행렬 A
    answer = [[i*N+j for j in range(1,N+1)] for i in range(N)] # 비교 행렬 answer
    cnt = 0 # 정렬에 필요한 횟수
    for n in range(N-1, 0, -1):
        if A[n][:n] != answer[n][:n]:
            for i in range(n+1):
                for j in range(i+1, n+1):
                    temp = A[i][j]
                    A[i][j] = A[j][i]
                    A[j][i] = temp
            cnt += 1   
    print(cnt)