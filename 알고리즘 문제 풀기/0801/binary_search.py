def binary_search(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:  # 검색 성공
            return True

        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False  # 검색 실패


def binary_search2(a, low, high, key):
    if low > high:  # 검색 실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:  # 검색 성공
            return True
        elif key < a[middle]:
            return binary_search2(a, low, middle - 1, key)
        elif a[middle] < key:
            return binary_search2(a, middle + 1, high, key)


arr = [i + i * 2 for i in range(10)]
print(binary_search(arr, len(arr), 15))
print(binary_search(arr, len(arr), 4))
print(binary_search2(arr, 0, len(arr), 15))
print(binary_search2(arr, 0, len(arr), 20))
