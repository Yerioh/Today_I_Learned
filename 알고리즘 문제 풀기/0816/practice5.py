TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())  # 수업을 들어야 하는 일수
    arr = list(map(int, input().split()))  # 각 요일별 수업 여부(일 ~ 토)
    answer = n * 7  # 지내야하는 최수 일수
    for i in range(7):
        idx = i
        cnt = 0  # 현재까지 수업을 들은 일수
        date = 0
        while cnt < n:
            if arr[idx] == 1:
                cnt += 1
            date += 1
            idx = (idx + 1) % 7
        if date < answer:
            answer = date
    print(f"#{tc} {answer}")
