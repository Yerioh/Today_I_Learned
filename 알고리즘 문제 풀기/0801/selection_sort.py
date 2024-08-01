def selection_sort(a, n):
    for i in range(n - 1):
        idx = i
        for j in range(i + 1, n):
            if a[idx] > a[j]:
                idx = j
        a[i], a[idx] = a[idx], a[i]
    return a


def select(a, k):
    for i in range(0, k):
        idx = i
        for j in range(i + 1, len(a)):
            if a[idx] > a[j]:
                idx = j
        a[i], a[idx] = a[idx], a[i]
    return a[k]


arr = [6, 3, 2, 4, 1, 5, 0]
print(selection_sort(arr, len(arr)))
print(select(arr, 4))
