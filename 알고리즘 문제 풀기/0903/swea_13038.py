import sys

sys.stdin = open("txt/in_13038.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    n = int(input())  # 수업을 들어야하는 일수
    class_day = list(map(int, input().split()))  # 각 요일에 수업이 열리는지 정보
    answer = n * 8
    # 수업이 열리는 날들을 찾아 그곳에서 시작하여 가장 작은 일수 찾기
    for i in range(7):
        days = 0  # 지내야 하는 날수
        if class_day[i]:  # 수업이 열리는 날이라면
            cnt = 0  # 수업을 얼마나 들었는지
            idx = i  # 현재 요일
            while cnt < n:
                days += 1
                if class_day[idx]:
                    cnt += 1
                idx = (idx + 1) % 7
        if days and days < answer:  # 0이 아니면서 최솟값
            answer = days
    print(f"#{tc} {answer}")
