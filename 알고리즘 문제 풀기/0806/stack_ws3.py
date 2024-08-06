import sys

sys.stdin = open('txt/input_ws3.txt', 'r')


def cal_(n, m):
    if m == 1:  # m이 1이면 재귀 종료
        return n
    else:  # m을 줄여가며 재귀
        return n * cal_(n, m - 1)


T = 10  # 테스트 케이스의 수
for _ in range(T):
    tc = int(input())  # 테스트 케이스의 번호
    N, M = map(int, input().split())  # 입력받은 N**M에 해당하는 값
    print(f'#{tc} {cal_(N, M)}')
