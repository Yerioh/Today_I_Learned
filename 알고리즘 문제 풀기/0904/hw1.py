import sys

sys.stdin = open("txt/in_hw1.txt", "r")

# 병합 정렬


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2  # 중간 인덱스
    left = arr[:mid]
    right = arr[mid:]
    # 각각 다시 정렬
    left = merge_sort(left)
    right = merge_sort(right)
    # 병합하여 리턴
    return merge(left, right)


def merge(left, right):
    global answer
    if left[len(left) - 1] > right[len(right) - 1]:
        answer += 1
    result = [0] * (len(left) + len(right))  # 결과를 담을 리스트
    li = ri = 0
    # 둘 다 고려할 때
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            result[li + ri] = left[li]
            li += 1
        else:
            result[li + ri] = right[ri]
            ri += 1
    # 왼쪽만 남을 때
    while li < len(left):
        result[li + ri] = left[li]
        li += 1
    # 오른쪽만 남을 때
    while ri < len(right):
        result[li + ri] = right[ri]
        ri += 1
    return result


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 정수의 개수 N
    A = list(map(int, input().split()))  # 정렬할 정수 리스트
    answer = 0  # 왼쪽 마지막 값의 크기가 오른쪽 마지막 값의 크기보다 큰 경우의 수
    print(f"#{tc} {merge_sort(A)[N // 2]} {answer}")
