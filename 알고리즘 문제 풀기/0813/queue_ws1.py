import sys

sys.stdin = open('txt/in_ws1.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기 N, 반복 횟수 M
    arr = list(map(int, input().split()))
    idx = 0  # 정답의 위치
    for i in range(M):
        idx = (idx + 1) % N
    print(f'#{tc} {arr[idx]}')
