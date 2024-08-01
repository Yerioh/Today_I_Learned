import sys

sys.stdin = open('txt/input_19003.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    answer = 0
    cnt = 0  # 자체 회문 cnt
    half_arr = []  # 반쪽 회문 리스트
    for s in arr:
        if s == s[::-1]:
            answer += M if cnt == 0 else 0 
            cnt += 1
        else:
            if s[::-1] in arr:
                answer += (M * 2) if s[::-1] not in half_arr  else 0
                half_arr.append(s)
    print(f'#{tc} {answer}')
