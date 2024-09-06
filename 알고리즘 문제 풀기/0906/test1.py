import sys

sys.stdin = open("txt/in_test1.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 식재료의 수
    foods = [list(map(int, input().split())) for _ in range(N)]  # 음식별 시너지
    answer = 20000 * N * N
    for target in range(1 << N):
        x = bin(target).count("1")  # 1의 개수가 N // 2이면 개수에 맞게 분배
        if x == N // 2:
            a = [0] * (N // 2)
            b = [0] * (N // 2)
            ai = bi = 0
            for i in range(N):
                if not target & (1 << i):  # 0이면 a재료
                    a[ai] = i
                    ai += 1
                if target & (1 << i):  # 1이면 b재료
                    b[bi] = i
                    bi += 1
            sum_a = 0
            sum_b = 0
            for i in range(N // 2):
                for j in range(N // 2):
                    if i != j:
                        sum_a += foods[a[i]][a[j]]
                        sum_b += foods[b[i]][b[j]]
            temp = abs(sum_a - sum_b)
            if temp < answer:
                answer = temp
    print(f"#{tc} {answer}")
