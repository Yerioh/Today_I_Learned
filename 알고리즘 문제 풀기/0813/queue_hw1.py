import sys

sys.stdin = open('txt/in_hw1.txt', 'r')

for _ in range(10):
    tc = '#' + input()
    arr = list(map(int, input().split()))
    front = rear = 0
    num = 0  # 감소하는 값
    while True:
        num = num % 5 + 1  # 1 2 3 4 5
        arr[front] -= num
        # 종료 조건
        if arr[front] <= 0:
            arr[front] = 0
            rear = front
            front = (front + 1) % 8
            break
        rear = front
        front = (front + 1) % 8
    answer = [0] * 8
    for i in range(8):
        answer[i] = arr[front]
        front = (front + 1) % 8
    print(tc, *answer)
