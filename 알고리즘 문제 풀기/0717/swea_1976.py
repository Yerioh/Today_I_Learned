import sys
sys.stdin = open("swea_1976.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 입력받은 시간의 리스트(시 분 시 분)
    time_list = list(map(int, input().split()))

    # 시간의 합 초기화
    time_sum = 0
    for i in range(len(time_list)):
        if i%2 == 0: # 인덱스 짝수는 시
            time_sum += (time_list[i] * 60)
        else:
            time_sum += time_list[i]
    print(f'#{t} {time_sum//60 if time_sum//60 <= 12 else time_sum//60 - 12} {time_sum%60}')