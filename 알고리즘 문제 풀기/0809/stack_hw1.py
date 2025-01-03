import sys

sys.stdin = open('txt/input_hw1.txt', 'r')

# 연산자의 우선순위
priority = {'+': 1, '*': 2}


def get_postfix(infix, n):
    postfix = ''
    stack = []
    for i in range(n):
        if infix[i] not in '+*':  # 숫자라면
            postfix += infix[i]
        else:
            # 스택에 값이 있고, 현재 연산자가 스택의 top 의 연산자보다 우선순위가 낮거나 같으면
            while stack and priority[infix[i]] <= priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(infix[i])
    # 남은 연산자 처리
    while stack:
        postfix += stack.pop()
    return postfix


def get_result(postfix):
    stack = []
    for token in postfix:
        if token not in '+*':
            stack.append(int(token))
        else:
            # 스택에서 숫자 두개 꺼내 계산
            right = stack.pop()
            left = stack.pop()
            result = 0
            if token == '+':
                result = left + right
            elif token == '*':
                result = left * right
            # 결과도 다음 연산에 사용해야 하므로
            stack.append(result)
    return stack.pop()


for tc in range(1, 11):
    N = int(input())  # 문자열의 길이
    infix1 = input()  # 입력받은 중위식
    postfix1 = get_postfix(infix1, N)
    answer = get_result(postfix1)
    print(f'#{tc} {answer}')
