import sys

sys.stdin = open('txt/input_18662.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    answer = abs((c + a) / 2 - b)
    print(f'#{tc} {answer}')
