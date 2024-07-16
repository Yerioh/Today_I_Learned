# 테스트 케이스의 수
T = int(input())
for t in range(1,T+1):
    # 입력 받은 정수 N
    N = int(input())
    # 답변 초기화
    answer = 0
    # 1부터 N까지 반복
    for i in range(1,N+1):
        if i%2 != 0:
            answer += i
        else:
            answer -= i
    print(f'#{t} {answer}')