"""
1부터 10까지 출력해보기
반복문 => 재귀 호출
"""

n = 10
print("반복문")
for i in range(1, n + 1):
    print(i, end=" ")
print()


def num_print(num, N):
    j = num
    if j > N:
        return
    else:
        print(j, end=" ")
        num_print(j + 1, n)


print("재귀 함수")
num_print(1, n)
print()
print()
"""
재귀 함수를 통해 2차원 배열 행 우선 순회해보기
"""

N = 6
arr = [[N * j + i for i in range(1, N + 1)] for j in range(N)]  # 1 ~ N*N

print("반복문 사용")
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()


def row_print(k, N):
    k += 1
    # k가 N * N 보다 크면 종료
    if k > N * N:
        return
    else:
        # k가 N의 배수라면 줄바꿈
        if k % N == 0:
            print(k)
        else:
            print(k, end=" ")
        row_print(k, N)


def row_print2(lst, ri, ci, N):
    print(lst[ri][ci], end=" ")
    # N-1, N-1이라면 종료
    if ri == N - 1 and ci == N - 1:
        return
    else:
        # ci가 마지막 인덱스라면 줄바꿈 및 ri 1증가, ci 초기화
        if ci == N - 1:
            ri += 1
            ci = -1
            print()
        ci += 1
        row_print2(lst, ri, ci, N)


print("재귀 함수")
row_print(0, N)
print("재귀 함수2")
row_print2(arr, 0, 0, N)
