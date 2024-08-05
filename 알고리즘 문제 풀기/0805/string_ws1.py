import sys

sys.stdin = open('txt/input_ws1.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    str1 = input()  # 길이가 N인 문자열
    N = len(str1)
    str2 = input()  # 길이가 M인 문자열
    M = len(str2)
    answer = 0  # 정답 초기값
    for i in range(M - N + 1):
        check = True
        for j in range(N):  # 한번이라도 다를 경우 False로 변경
            if str2[i + j] != str1[j]:
                check = False
        if check:
            answer = 1
    print(f'#{tc} {answer}')
