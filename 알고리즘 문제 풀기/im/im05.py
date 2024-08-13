import sys

sys.stdin = open('txt/in05.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]  # 5개의 문자열
    answer = ''
    l = 0  # 가장 긴 문자열의 길이
    for word in arr:
        if l < len(word):
            l = len(word)
    # 열순회
    for c in range(l):
        for r in range(5):
            if c < len(arr[r]):  # 인덱스 범위 내라면
                answer += arr[r][c]
    print(f'#{tc} {answer}')
