"""
3
1
17
2020

"""
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 두 합성수의 차
    # N * i - N * (i - 1) == N
    # 차가 1인 합성수 중 가장 작은 값들은 9, 8
    answer1, answer2 = N*9, N*8
    print(f"#{tc} {answer1} {answer2}")
