import sys

sys.stdin = open("txt/in09.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 돌아가야할 학생들의 수
    arr = [0] * 200  # 각 학생들의 이동 경로 배열
    for _ in range(N):
        s, e = map(int, input().split())
        s, e = (s - 1) // 2, (e - 1) // 2  # 인덱스 기준, 몫이 같을 경우 복도 공유
        for i in range(200):
            if min(s, e) <= i <= max(s, e):  # 뒷방에서 앞방으로 이동할 수도 있음
                arr[i] += 1
    answer = 0  # 각 학생이 복도를 겹치는 최댓값이 모든 학생이 이동하는 최소 단위 시간
    for num in arr:
        if num > answer:
            answer = num
    print(f"#{tc} {answer}")
