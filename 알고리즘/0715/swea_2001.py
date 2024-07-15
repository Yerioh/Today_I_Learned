import sys
sys.stdin = open("swea_2001.txt", "r")

# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.
T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    li =  [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_fly = 0
            sum_fly += (li[i][j])
