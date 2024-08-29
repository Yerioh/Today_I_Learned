"""
3
0.625
0.1
0.125

#1 101
#2 overflow
#3 001
"""
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = float(input())  # 입력 받은 0 < 십진수 < 1
    answer = ""
    i = 1
    # 주어진 소수를 1/ 2^n으로 나누었을때 몫을 2진수로 나머지를 계속 진행
    while N > 0:
        num = 2 ** i
        answer += str(int(N // (1 / num)))
        i += 1
        N %= 1 / num
        if len(answer) == 13:
            answer = "overflow"
            break
    print(f"#{tc} {answer}")
