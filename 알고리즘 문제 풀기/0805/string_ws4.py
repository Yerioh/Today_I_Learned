import sys

sys.stdin = open('txt/input_ws4.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    answer = 0
    i = 0
    while i < len(A):
        # 인덱스 범위를 벗어나면 마지막 인덱스까지만 확인
        check_word = A[i: i + len(B)] if i + len(B) < len(A) else A[i:] 
        # B와 같다면 인덱스를 해당 길이만큼 뒤로
        if check_word == B:
            i += len(B)
        # 다르다면 인덱스를 하나만 뒤로
        else:
            i += 1
        answer += 1
    print(f'#{tc} {answer}')
