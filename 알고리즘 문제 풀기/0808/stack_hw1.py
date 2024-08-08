import sys

sys.stdin = open('txt/input_hw1.txt', 'r')


# 후위 표현식 구하기
def get_postfix(infix, n):
    postfix = ''
    stack = 0  # 더하기의 수 저장
    for i in range(n):
        # 더하기면 저장
        if infix[i] == '+':
            stack += 1
        else:
            postfix += infix[i]
            # 더하기가 저장되어 있다면
            if stack:
                postfix += '+'
                stack -= 1
    if stack:
        return 'Error'
    return postfix


# 후위 표현식 계산하기
def cal_postfix(postfix):
    stack = [' ', ' ']  # 두 개 초과의 수가 들어가지 않음
    for token in postfix:
        if token == '+':
            result = stack[0] + stack[1]
            stack[0] = result
        else:
            if stack[0] != ' ':  # stack[0]은 한 번 삽입 후에 비워질수 없음을 이용
                stack[1] = int(token)
            else:
                stack[0] = int(token)
    return stack[0]


for tc in range(1, 11):
    N = int(input())  # 문자열의 길이
    infix1 = input()  # 중위표현식 문자열
    postfix1 = get_postfix(infix1, N)
    # 제대로 된 표현식이 만들어지지 않으면 실행되지 않음
    if postfix1 == 'Error':
        print('Error!!!')
        continue
    answer = cal_postfix(postfix1)
    print(f'#{tc} {answer}')
