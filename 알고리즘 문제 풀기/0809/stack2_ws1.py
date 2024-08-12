import sys

sys.stdin = open('txt/input_ws1.txt', 'r')


def min_sum_array(c, selected, result, n):
    global answer
    s = 0
    for num in result:
        s += num
    if c == n:
        if s < answer:
            answer = s
        return
    # 숫자를 다 정하지 않았을 때, 최소값보다 합이 크거나 같다면 종료
    if s >= answer:
        return
    # 자리를 정할 열의 행 순회
    for r in range(N):
        if not selected[r]:
            selected[r] = 1
            result.append(arr[r][c])
            min_sum_array(c + 1, selected, result, n)
            # 다음 경우를 위해 초기화
            selected[r] = 0
            result.pop()


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 입력받은 2차원 배열
    answer = 10 * N  # 각 수는 10보다 작으므로 정답은 10N 보다 클 수 없다.
    min_sum_array(0, [0] * N, [], N)
    print(f'#{tc} {answer}')
