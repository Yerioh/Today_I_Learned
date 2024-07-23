import sys
sys.stdin = open('input_20551.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 각 상자의 사탕 수
    A, B, C = map(int, input().split())
    # 정답 초기화
    answer = 0
    # C가 B 이하면 둘의 차이의 +1 만큼 먹음
    if C <= B:
        eat_B = B - C + 1
        B = B - eat_B
        # B가 0이면 불가능
        if B:
            answer += eat_B
        else:
            answer = -1
    # 이미 불가능하면 실행 X
    if answer != -1:
        # 먹고 난 후의 B가 A 이하면 둘의 차이의 +1 만큼 먹음
        if B <= A:
            eat_A = A - B + 1
            A = A - eat_A
            # A가 0이면 불가능
            if A:
                answer += eat_A
            else:
                answer = -1
    print(f'#{t} {answer}') 