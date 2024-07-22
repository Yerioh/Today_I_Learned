import sys
sys.stdin = open('input_1285.txt','r')

T = int(input())
for t in range(1, T+1):
    # 돌을 던지는 사람의 수
    N = int(input())
    # 각 사람이 돌을 던진 위치
    stone_list = list(map(int, input().split()))
    # 각 위치와 기준점과의 거리
    distance_list = list(map(lambda x: abs(0-x), stone_list))
    
    print(f'#{t} {min(distance_list)} {distance_list.count(min(distance_list))}')
