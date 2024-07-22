import sys
sys.stdin = open('input_1284.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1): 
    # A사 금액 P, B사 기본 금액 Q, 기본사용량 R, 초과량당 금액 S, 사용량W 
    P, Q, R, S, W = map(int,input().split())
    A = P*W
    B = Q
    if  W > R:
        B += (W-R)*S
    answer = A if A <= B else B
    print(f'#{t} {answer}')