import sys

sys.stdin = open("txt/in_test3.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 방의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # 방 안의 정보
    S = []  # 계단 정보 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 1:  # 2이상은 계단이다
                S.append((i, j, arr[i][j]))  # 계단 좌표, 길이 저장
    P1 = []  # 계단1로 가는 사람 정보
    P2 = []  # 계단2로 가는 사람 정보
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                temp = [0, 0, 0, 100]  # 사람의 좌표, 계단 번호, 걸리는 시간
                for s in range(2):  # 각 계단까지 걸리는 시간 비교
                    m = abs(i - S[s][0]) + abs(j - S[s][1])
                    if temp[3] > m:
                        temp = [i, j, s, m]
                if temp[2]:
                    P2.append(temp)
                else:
                    P1.append(temp)
    P1.sort(key=lambda x: x[3])
    P2.sort(key=lambda x: x[3])
    answer = 0
    S1 = []  # 현재 1번 계단 위에 있는 사람
    S2 = []  # 현재 2번 계단 위에 있는 사람
    while P1 or P2 or S1 or S2:
        answer += 1
        p1 = p2 = 0
        for i in range(len(P1)):
            if P1[i][3] + 1 == answer:
                S1.append(arr[S[0][0]][S[0][1]] + 1)
                p1 += 1
        for _ in range(p1):
            P1.pop(0)
        for i in range(len(P2)):
            if P2[i][3] + 1 == answer:
                S2.append(arr[S[1][0]][S[1][1]] + 1)
                p2 += 1
        for _ in range(p2):
            P2.pop(0)
        s1 = s2 = 0
        for i in range(len(S1)):
            S1[i] -= 1
            if not S1[i]:
                s1 += 1
        for _ in range(s1):
            S1.pop(0)
        for i in range(len(S2)):
            S2[i] -= 1
            if not S2[i]:
                s2 += 1
        for _ in range(s2):
            S2.pop(0)
    print(f"#{tc} {answer}")
