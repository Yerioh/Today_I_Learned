import sys
sys.stdin = open("input_1959.txt", "r")

# 테스트케이스의 수
T = int(input())
for t in range(1, T+1):
    # 입력 받은 정수 N, M
    N, M = map(int, input().split())
    # 두 리스트 입력
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))

    # 숫자 계산 함수
    def cal_num(list_1, list_2):
        answer = 0
        for i in range(len(list_2)-len(list_1)+1):
            num_sum = 0
            for j in range(len(list_1)):
                num_sum += (list_1[j] * list_2[i+j])
            if answer < num_sum:
                answer = num_sum
        return answer
    
    # N, M 크기를 비교하여 함수 호출
    if N <= M:
        print(f'#{t} {cal_num(list_n, list_m)}')
    else:
        print(f'#{t} {cal_num(list_m, list_n)}')




