import sys

sys.stdin = open('txt/input_ws4.txt', 'r')

for tc in range(1, 11):
    N, arr = input().split()
    N = int(N)  # 정수로 변환
    arr = list(arr)  # 리스트로 변환
    answer = ''  # 정답 및 스택
    top = -1  # 마지막 스택 위치
    for i in range(N):
        # 스택이 쌓여있고 스택의 현재 값과 배열의 현재 값이 같다면
        if top >= 0 and answer[top] == arr[i]:
            # 스택에서 마지막 값 제거
            answer = answer[:top]
            # 스택 위치 감소
            top -= 1
        else:
            # 스택 누적
            answer += arr[i]
            # 스택 위치 증가
            top += 1
    print(f'#{tc} {answer}')
