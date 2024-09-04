import sys

sys.stdin = open("txt/in_ws2.txt", "r")


# 백만 개의 정수 정렬


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


A = list(map(int, input().split()))  # 백만개 수 리스트
print(merge_sort(A)[500000])
