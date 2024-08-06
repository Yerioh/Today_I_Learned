T = int(input())
for tc in range(1, T + 1):
    check = input()
    stack = []

    # 괄호 검사 결과 : 1이면 ok, 0이면 err
    answer = 1

    # 괄호 검사
    for c in check:
        # c가 여는 괄호인가?
        if c in ['(', '{']:
            stack.append(c)
        # c가 닫는 괄호인가?
        elif c in [')', '}']:
            # 스택에서 꺼내기 전에 스택이 비어있나 확인
            if not stack:
                answer = 0
            # 비어있지 않으면 꺼내와서 짝이 맞는지 검사
            else:
                temp = stack.pop()
                if temp == '(':
                    answer = 0 if c != ')' else answer
                elif temp == '{':
                    answer = 0 if c != '}' else answer
    # 반복 종료 후 스택이 비어있나 확인
    if stack:
        answer = 0
    print(f'#{tc} {answer}')
