import sys
sys.stdin = open("swea_2001.txt", "r")

# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.
# 테스트 케이스 수
T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split()) # n: 영역 전체, m: 파리채 크기
    li =  [list(map(int, input().split())) for _ in range(n)] # 각 영역 안의 파리 수
    sum_fly_list = [] # 기준점 기준으로 파리채로 잡은 파리 합
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_fly = 0 # 파리의 합
            for k in range(m):
                sum_fly += sum(li[i+k][j:j+m])
            sum_fly_list.append(sum_fly)
    print(f"#{t} {max(sum_fly_list)}")
            
