"""
3
11 34 23 81 28 34
11 45 22 81 23 34 99 22 17 8
1 1 1 1 1 0 0 0 0 0

"""
# 배열의 데이터를 퀵 정렬하는 함수를 작성하고 테스트 해보시오.


def partitioning(left, right):
    pivot = arr[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= j and arr[i] <= pivot:  # 큰 값 탐색
            i += 1
        while i <= j and arr[j] >= pivot:  # 작은 값 탐색
            j -= 1
        if i < j:  # 탐색 과정 중에만 교환하기 위해서
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(left, right):
    if left < right:
        pivot = partitioning(left, right)  # 정렬 후 pivot 인덱스 가져오기
        quick_sort(left, pivot - 1)  # 왼쪽을 정렬
        quick_sort(pivot + 1, right)  # 오른쪽을 정렬


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    quick_sort(0, len(arr) - 1)
    print(f"#{tc} {arr}")
