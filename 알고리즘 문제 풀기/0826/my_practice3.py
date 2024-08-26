import sys

sys.stdin = open("txt/in03.txt", "r")

TC = int(input())  # 테스트 케이스의 수
for tc in range(1, TC + 1):
    N = int(input())  # 전선의 개수
    arr = [list(map(int, input().split())) for _ in range(N)]  # 각 전선의 전봇대에서의 위치
    arr.sort(key=lambda x: x[0])  # A를 기준으로 정렬
    answer = 0
    for i in range(N):
        for j in range(i, N):  # 자기 다음 전선들과 비교
            if arr[i][1] > arr[j][1]:  # 기준 b보다 낮다면 교차하는 것
                answer += 1
    print(f"#{tc} {answer}")
