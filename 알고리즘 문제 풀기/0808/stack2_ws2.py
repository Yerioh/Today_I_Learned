import sys

sys.stdin = open('txt/input_ws2.txt', 'r')


def postfix_cal(postfix):
    stack = []
    result = 0
    for token in postfix:
        # 숫자일 경우 push
        if token not in '+-*/.':
            stack.append(int(token))
        else:
            if token == '.':
                continue
            # stack 에 2개 이상의 수가 없다면 error
            if len(stack) < 2:
                return 'error'
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = int(num1 / num2)
            stack.append(result)
    # 스택에 2개 이상의 수가 남아있다면
    if len(stack) >= 2:
        return 'error'
    return stack.pop()



T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    expression = input().split()  # 수식 리스트로 받기
    answer = postfix_cal(expression)
    print(f'#{tc} {answer}')
