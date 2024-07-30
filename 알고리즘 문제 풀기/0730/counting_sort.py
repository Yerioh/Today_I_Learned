def counting_sort(data, k):
    counts = [0] * k  # data 가 0~k 까지의 정수
    # data 의 각 요소들의 개수를 counts 에 저장
    for num in data:
        counts[num] += 1
    # counts 를 각 요소의 위치를 계산하기 쉽게 변형(앞 요소까지의 수를 누적)
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    # data 를 뒤에서 부터 순회하고 counts 를 통해 각 요소의 위치를 결정하여 temp 에 저장
    temp = [0] * len(data)
    for num in data[::-1]:   # for i in range(len(data) - 1, -1, -1):
        counts[num] -= 1         # counts[data[i]] -= 1
        temp[counts[num]] = num  # temp[counts[data[i]]] = data[i]
    return temp


numbers = [0, 4, 1, 3, 1, 2, 4, 1]
print(*counting_sort(numbers, max(numbers) + 1))
