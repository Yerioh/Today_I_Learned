import sys

sys.stdin = open('txt/input_ap3.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = input()  # 쇠막대와 레이제 문자열
    answer = 0  # 정답 초기화
    cur_stick = 0  # 현재 쇠막대 개수
    i = 0  # 배열의 현재 위치
    while i < len(arr):
        # 레이저인지 확인
        if arr[i] == '(' and arr[i + 1] == ')':
            # 레이저라면 현재 막대 개수를 정답에 더함
            answer += cur_stick
            # 레이저 다음으로 이동하기 위해
            i += 1
        # 레이저가 아니고 막대가 생겼다면 현재 막대 증가
        elif arr[i] == '(':
            cur_stick += 1
        # 레이저가 아니고 막대가 끝났다면 정답 증가, 현재 막대 감소
        elif arr[i] == ')':
            answer += 1
            cur_stick -= 1
        # 다음으로 이동
        i += 1
    print(f'#{tc} {answer}')
