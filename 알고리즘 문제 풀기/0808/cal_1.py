# 우선 순위 표
# ()>*/+-

# 스택 밖에 있을 때 우선순위
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
# 스택 안에 있을 때 우선순위
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}


# 중위 표기식(infix) => 후위 표기식(postfix)
# n: 식의 길이
def get_postfix(infix, n):
    # 결과를 출력할 후위 표기식
    postfix = ''

    stack = []

    # 문자열에서 하나씩 떼어와서 식 만들자
    for i in range(n):
        # i번째 글자가 피연산자
        if infix[i] not in "(+-*/)":
            postfix += infix[i]
        else:
            # i번째 글자가 닫는 괄호인가?
            if infix[i] == ')':
                # 여는 괄호가 나올때 까지 pop 해서 결과에 출력
                while stack:
                    # 연산자 하나 꺼내기
                    op = stack.pop()
                    # 여는 괄호이면 중단
                    if op == '(':
                        break
                    else:
                        postfix += op
            # i번째 글자가 연산자다 => 우선순위 보고 판별
            else:
                # 현재 연산자의 우선순위보다
                # 스택의 top 에 있는 연산자의 우선순위가 같거나 높으면
                # pop 해서 출력한다 => 우선순위가 높은 연산자를 먼저 계산하기 때문
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()

                # 스택에 top 에 있는 연산자의 우선순위가 나보다 작으면
                # 위에서 우선순위가 같거나 높은 것은 제거
                stack.append(infix[i])
    # 스택에 남은 연산자 모두 출력
    while stack:
        postfix += stack.pop()

    return postfix


infix1 = '(6+5*(2-8)/2)'
postfix1 = get_postfix(infix1, len(infix1))
print(postfix1)


# 후위 표기식 계산
def get_result(postfix):
    stack = []
    # 후위표기식에서 글자 하나씩 떼어오기
    for token in postfix:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            result = 0
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            stack.append(result)
    return stack.pop()


print(get_result(postfix1))
