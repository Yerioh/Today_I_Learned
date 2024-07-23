import sys
sys.stdin = open('input_20934.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    S, K = input().split()
    K = int(K)
    
    cup = S
    # 방울이 울린 만큼 반복
    for i in range(K):
        if cup.index('o') == 0:
            cup = '.o.'
        elif cup.index('o') == 2:
            cup = '.o.'
        else: # 방울이 가운데 있을 경우 무조건 왼쪽으로
            cup = 'o..'
    print(f'#{t} {cup.index("o")}')