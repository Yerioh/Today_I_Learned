T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 만들어야 하는 가로의 길이
    answer = 1
    # 자신의 다음 값을 구하는 방법
    for i in range(1, N // 10):
        # 자신이 홀수번째이면 자신 + 1을 더하고, 짝수번째이면 자신 - 1을 더한다.
        answer += (answer + 1) if i % 2 else (answer - 1)
    print(f'#{tc} {answer}')
