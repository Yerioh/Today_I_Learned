import sys

sys.stdin = open('txt/input_ws2.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    s = input()  # 입력받은 문자열 s
    stack = ''  # 문자를 쌓을 stack
    for i in range(len(s)):
        # stack 의 마지막 글자와 현재 글자가 같다면
        if len(stack) != 0 and stack[-1] == s[i]:
            # stack 의 마지막 글자 제외하고 할당
            stack = stack[:-1]
        else:
            stack += s[i]
    answer = len(stack)
    print(f'#{tc} {answer}')


