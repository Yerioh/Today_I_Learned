import sys
sys.stdin = open('input_1940.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    N = int(input())
    command_list = [list(map(int, input().split())) for _ in range(N)]

    # 움직인 거리
    answer = 0
    # 현재 속도
    speed = 0
    for command in command_list:
        if command[0] == 1:
            speed += command[1]
            answer += speed
        elif command[0] == 2:
            speed -= command[1]
            if speed < 0:
                speed = 0
            answer += speed
        else:
            answer += speed
    print(f'#{t} {answer}')