import sys

sys.stdin = open('txt/input_ws2.txt', 'r')


def tournament(i, j):
    # i와 j가 같다면 그룹 분할 끝
    if i == j:
        return i
    else:
        left = tournament(i, (i + j) // 2)
        right = tournament((i + j) // 2 + 1, j)
        # right 가 이기는 경우를 제외하면 left 가 이긴다
        if arr[left] == 1:  # left 가위
            if arr[right] == 2:  # right 바위
                return right
            else:
                return left
        elif arr[left] == 2:  # left 바위
            if arr[right] == 3:  # right 보
                return right
            else:
                return left
        elif arr[left] == 3:  # left 보
            if arr[right] == 1:  # right 가위
                return right
            else:
                return left


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 게임에 참가한 사람 수 N
    arr = list(map(int, input().split()))  # 각 인원이 고른 카드
    answer = tournament(0, N - 1) + 1  # 각 사람의 번호는 인덱스 + 1
    print(f'#{tc} {answer}')
