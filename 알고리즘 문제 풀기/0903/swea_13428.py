import sys

sys.stdin = open("txt/in_13428.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = list(input())  # 입력받은 정수를 리스트로
    n = len(N)  # 리스트의 길이
    max_num = int("".join(N))
    min_num = int("".join(N))
    # 교환할 자리 찾기
    for i in range(n - 1):
        for j in range(i + 1, n):
            N[i], N[j] = N[j], N[i]  # 교환 해보기
            if N[0] != "0":  # 맨 앞은 0이 올 수 없다
                M = int("".join(N))
                if M > max_num:  # 최댓값 교환
                    max_num = M
                if M < min_num:  # 최솟값 교환
                    min_num = M
            N[i], N[j] = N[j], N[i]  # 교환 초기화
    print(f"#{tc} {min_num} {max_num}")
