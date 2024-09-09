"""
4
3 2 1
1 2 3
3 5 5
5 6 6

#1 -1
#2 0
#3 1
#4 2
"""


# 증가하는 사탕 수열
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    answer = 0
    if B >= C:  # B 가 C 보다 크면 작아질 만큼 먹어라
        answer += B - C + 1
        B -= B - C + 1
    if A >= B:  # A가 B 보다 크면 작아질 만큼 먹어라
        answer += A - B + 1
        A -= A - B + 1
    if A <= 0 or B <= 0:  # 둘 중 하나라도 0이하라면
        answer = -1
    print(f"#{tc} {answer}")
