import sys

sys.stdin = open("txt/in_pr3.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    K = int(input())  # 회전 시킬 수
    # n극 : 0, s극 : 1
    m1 = list(map(int, input().split()))
    m2 = list(map(int, input().split()))
    m3 = list(map(int, input().split()))
    m4 = list(map(int, input().split()))
    # 처음 화살표 위치는 0
    a1 = a2 = a3 = a4 = 0
    D = [0, 0, 0, 0]
    for _ in range(K):
        k, d = map(int, input().split())
        d1 = d2 = d3 = d4 = 0
        if k == 1:
            d1 = d
            d2 = 0 if m1[(a1 + 2) % 8] == m2[(a2 + 6) % 8] else -1 if d1 == 1 else 1
            d3 = 0 if d2 == 0 or m2[(a2 + 2) % 8] == m3[(a3 + 6) % 8] else -1 if d2 == 1 else 1
            d4 = 0 if d3 == 0 or m3[(a3 + 2) % 8] == m4[(a4 + 6) % 8] else -1 if d3 == 1 else 1
        elif k == 2:
            d2 = d
            d1 = 0 if m1[(a1 + 2) % 8] == m2[(a2 + 6) % 8] else -1 if d2 == 1 else 1
            d3 = 0 if m2[(a2 + 2) % 8] == m3[(a3 + 6) % 8] else -1 if d2 == 1 else 1
            d4 = 0 if d3 == 0 or m3[(a3 + 2) % 8] == m4[(a4 + 6) % 8] else -1 if d3 == 1 else 1
        elif k == 3:
            d3 = d
            d2 = 0 if m2[(a2 + 2) % 8] == m3[(a3 + 6) % 8] else -1 if d3 == 1 else 1
            d1 = 0 if d2 == 0 or m1[(a1 + 2) % 8] == m2[(a2 + 6) % 8] else -1 if d2 == 1 else 1
            d4 = 0 if m3[(a3 + 2) % 8] == m4[(a4 + 6) % 8] else -1 if d3 == 1 else 1
        elif k == 4:
            d4 = d
            d3 = 0 if m3[(a3 + 2) % 8] == m3[(a3 + 6) % 8] else -1 if d4 == 1 else 1
            d2 = 0 if d3 == 0 or m2[(a2 + 2) % 8] == m3[(a3 + 6) % 8] else -1 if d3 == 1 else 1
            d1 = 0 if d2 == 0 or m1[(a1 + 2) % 8] == m2[(a2 + 6) % 8] else -1 if d2 == 1 else 1
        a1 = a1 - d1
        a1 = a1 % 8 if a1 >= 0 else 7
        a2 = a2 - d2
        a2 = a2 % 8 if a2 >= 0 else 7
        a3 = a3 - d3
        a3 = a3 % 8 if a3 >= 0 else 7
        a4 = a4 - d4
        a4 = a4 % 8 if a4 >= 0 else 7
    answer = m1[a1] + m2[a2] * 2 + m3[a3] * 4 + m4[a4] * 8
    print(f"#{tc} {answer}")
