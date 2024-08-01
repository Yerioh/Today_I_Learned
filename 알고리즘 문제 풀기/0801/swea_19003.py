import sys

sys.stdin = open('txt/input_19003.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    arr = input().split()
    answer = 0
    for i in range(1, 1 << N):
        s = ''
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
        l = len(s)
        reverse_s = ''
        for j in range(l):
            reverse_s += s[l - 1 - i]
        if reverse_s == s and l > answer:
            answer = l
    print(f'#{tc} {l}')
