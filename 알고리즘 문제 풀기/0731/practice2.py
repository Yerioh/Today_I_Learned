import sys

# 부분 집합 만들기
arr1 = [1, 2, 3, 4]
bit1 = [0] * len(arr1)


def mk_subset(arr, bit):
    new_arr = [" "] * len(arr)
    for i in range(len(arr)):
        if bit[i]:
            new_arr[i] = arr[i]
    return new_arr


for i in range(2):
    bit1[0] = i
    for j in range(2):
        bit1[1] = j
        for k in range(2):
            bit1[2] = k
            for l in range(2):
                bit1[3] = l
                print(mk_subset(arr1, bit1))


# 비트 연산자 사용
arr2 = [3, 6, 7, 1, 5, 4]
n = len(arr2)
for i in range(1 << n):
    for j in range(n):
        if i & (1 << j):
            print(arr2[j], end=" ")
    print()
print()


# 부분 집합의 합 만들기
def check_subset_sum_zero(arr, n):
    count_zero = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        if subset != [] and sum(subset) == 0:
            count_zero += 1
    return count_zero


sys.stdin = open('in2.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = 10
    number_set = list(map(int, input().split()))
    print(f'#{t} 합이 0인 부분집합의 수 : {check_subset_sum_zero(number_set, N)}')
