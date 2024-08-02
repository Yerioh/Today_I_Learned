import sys

sys.stdin = open('txt/input_ws1.txt', 'r')


def check_palindrome(my_str, m):
    check = True
    for i in range(m // 2):
        # 앞 뒤 비교
        if my_str[i] != my_str[m - 1 - i]:
            check = False
    return check


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기 N, 찾을 문자열의 길이 M
    str_arr = [input() for _ in range(N)]
    answer = ''  # 정답 초기화
    for i in range(N):
        for j in range(N):  # 문자열의 첫 위치
            row_str = ''
            col_str = ''
            for k in range(M):  # 필요한 길이만큼 반복하여 문자열 완성
                if j + k < N:  # IndexError 방지
                    row_str += str_arr[i][j + k]
                if i + k < N:  # IndexError 방지
                    col_str += str_arr[i + k][j]
            # 길이가 맞고, 회문이라면
            if len(row_str) == M and check_palindrome(row_str, M):
                answer = row_str
            if len(col_str) == M and check_palindrome(col_str, M):
                answer = col_str
    print(f'#{tc} {answer}')
