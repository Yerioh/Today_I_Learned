import sys

sys.stdin = open("txt/in_ws3.txt", "r")

# 퀵 정렬


def partitioning(left, right):
    # 기준 값
    pivot = A[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= j and A[i] <= pivot:  # 작은 값 찾기
            i += 1
        while i <= j and A[j] >= pivot:  # 큰 값 찾기
            j -= 1
        if i < j:  # 교환 가능할 때만
            A[i], A[j] = A[j], A[i]
    A[left], A[j] = A[j], A[left]
    return j


def quick_sort(start, end):
    if start < end:
        pivot = partitioning(start, end)
        quick_sort(start, pivot - 1)  # 왼쪽 정렬
        quick_sort(pivot + 1, end)  # 오른쪽 정렬


T = int(input())  # 테스트케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 정수의 개수
    A = list(map(int, input().split()))  # 정수 리스트
    quick_sort(0, N - 1)
    answer = A[N // 2]
    print(f"#{tc} {answer}")
