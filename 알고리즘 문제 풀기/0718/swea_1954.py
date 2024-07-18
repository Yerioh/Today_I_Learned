import sys
sys.stdin = open("input_1954.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num = (N+1)/2 if N%2!=0 else N/2
    # 값을 담을 리스트 N * N
    answer = [[" " for _ in range(N)] for _ in range(N)]

    # 리스트 값에 할당할 수
    count = 1
    # 반복할 횟수
    end_num = N
    # 반복 방향
    state = 'right'
    # 값을 담을 리스트의 위치
    idx = [0, 0]
    for i in range(int(num)):
        if end_num == 0:
            break
        # 방향에 따라 반복문 실행
        if state == 'right':
            for i in range(end_num):
                answer[idx[0]][idx[1]] = str(count)
                count += 1
                # 마지막 시행이라면
                if i == end_num-1:
                    idx[0] += 1
                    state = 'down'
                    end_num -= 1
                else:
                    idx[1] += 1
        if state == 'down':
            for i in range(end_num):
                answer[idx[0]][idx[1]] = str(count)
                count += 1
                # 마지막 시행이라면
                if i == end_num-1:
                    idx[1] -= 1
                    state = 'left'
                else:
                    idx[0] += 1
        if state == 'left':
            for i in range(end_num):
                answer[idx[0]][idx[1]] = str(count)
                count += 1
                # 마지막 시행이라면
                if i == end_num-1:
                    idx[0] -= 1
                    state = 'up'
                    end_num -= 1
                else:
                    idx[1] -= 1
        if state == 'up':
            for i in range(end_num):
                answer[idx[0]][idx[1]] = str(count)
                count +=1
                # 마지막 시행이라면
                if i == end_num-1:
                    idx[1] += 1
                    state = 'right'
                else:
                    idx[0] -= 1
    print(f'#{t}')
    for i in range(N):
        print(" ".join(answer[i]))