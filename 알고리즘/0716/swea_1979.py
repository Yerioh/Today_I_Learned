import sys
sys.stdin = open("swea_1979.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 퍼즐의 크기 N, 글자의 수 K
    N, K = map(int, input().split())
    # 퍼즐 모양 리스트
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 답변
    answer = 0
    for i in range(N):
        for j in range(N):
            count1 = 0 # 가로 카운트
            count2 = 0 # 세로 카운트
            for k in range(j, N): # 가로 계산
                if puzzle[i][k] == 1:
                    count1 += 1
                else:
                    break
            if j != 0 and puzzle[i][j-1] == 1:
                count1 = 0 
            for k in range(i, N): # 세로 계산
                if puzzle[k][j] == 1:
                    count2 += 1
                else:
                    break
            if i != 0 and puzzle[i-1][j] == 1:
                count2 = 0
            if count1 == K:
                answer += 1
            if count2 == K:
                answer += 1
    print(f'#{t} {answer}')