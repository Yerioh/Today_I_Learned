import sys

sys.stdin = open("txt/in02.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 카드이 수 N
    arr = input().split()  # 첫 카드의 배열
    answer = [0] * N
    p = (N + 1) // 2  # 반으로 가르는 기준
    d1, d2 = arr[:p], arr[p:]
    idx = 0  # 정답 배열의 인덱스
    for i in range(p):
        answer[idx] = d1[i]
        idx += 1
        if i < len(d2):
            answer[idx] = d2[i]
            idx += 1
    print(f"#{tc}", *answer)
