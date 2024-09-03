import sys

sys.stdin = open("txt/in_ws1.txt" ,"r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 신청 수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 각 화물차의 작업 시각
    arr.sort(key=lambda x: x[1])  # 종료시간 기준으로 정렬
    answer = 1  # 최소 한대의 화물차는 작업
    end_time = arr[0][1]  # 정렬했을 때 가장 앞에 있는 화물차의 종료시간
    for i in range(1, N):  # 다음 화물차부터 끝까지 검사
        # 다음 화물차의 시작시간이 작업중인 화물차의 종료시간보다 크다면 작업 가능
        if arr[i][0] >= end_time:
            answer += 1
            end_time = arr[i][1]  # 종료시간 변경
    print(f"#{tc} {answer}")
