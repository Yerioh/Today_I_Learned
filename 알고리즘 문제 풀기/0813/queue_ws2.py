import sys

sys.stdin = open('txt/in_ws2.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기 N, 피자 개수 M
    arr = list(map(int, input().split()))  # 각 피자의 치즈 수
    q = [0] * N  # 화덕의 역할을 할 큐
    idx_q = [0] * N  # 피자 번호를 담은 큐
    rear = 0
    idx = 0  # 다음에 들어갈 피자
    while True:
        if q[rear]:  # 피자가 들어있는 경우
            q[rear] //= 2
        if idx < M and not q[rear]:  # 남은 피자가 있고, 피자가 없거나 다 구워지면 새 피자 넣기
            q[rear] = arr[idx]
            idx_q[rear] = idx + 1
            idx += 1
        if q == [0] * N:  # 더 이상 넣을 피자가 없으면 종료
            break
        rear = (rear + 1) % N  # 다음 반복에 확인할 화덕의 위치
    print(f'#{tc} {idx_q[rear]}')
