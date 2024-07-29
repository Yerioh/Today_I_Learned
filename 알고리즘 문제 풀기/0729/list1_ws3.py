import sys
sys.stdin = open('input_ws3.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for t in range(1, T+1):
    N = int(input())  # 입력받은 정수 N
    num_list = [2, 3, 5, 7, 11]  # 계산을 위한 수 리스트
    answer = [0 for _ in range(5)]  # 정답을 담을 리스트
    for i in range(5):
        cnt = 0
        while not N % num_list[i]:  # 각 수를 나눌 수 있을 때까지 반복
            N /= num_list[i]
            cnt += 1
        answer[i] = cnt
    print(f'#{t}', end=" ")
    print(*answer)