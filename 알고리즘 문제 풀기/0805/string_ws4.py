T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    answer = 0
    i = 0
    while i < len(A):
        check = True
        if i + len(B) < len(A):
            for j in range(len(B)):
                if A[i + j] != B[j]:
                    check = False
        if check:
            i += len(B)
        else:
            i += 1
        answer += 1
    print(f'#{tc} {answer}')
