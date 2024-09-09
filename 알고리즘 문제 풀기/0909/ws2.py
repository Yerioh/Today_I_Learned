"""
3
1 3 5 7
0 5 2 4
0 5 1 6

#1 0
#2 2
#3 4
"""
# 두 전구
T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())  # X는 A에서 B까지, Y는 C에서 D까지
    result = min(B, D) - max(A, C) if B > C and D > A else 0
    answer[tc - 1] = f"#{tc} {result}"
print(*answer, sep="\n")
