import sys
sys.stdin = open('input_hw1.txt', 'r')

for t in range(1, 11):
    N = int(input())  # 건물의 개수 N
    arr = list(map(int, input().split()))  # 각 건물의 크기를 담은 배열
    view_sum = 0
    for i in range(2, N-2):
        left_side = arr[i] - (arr[i-2] if arr[i-2] > arr[i-1] else arr[i-1])  # 왼쪽 두 건물 중 더 높은 건물로 계산
        right_side = arr[i] - (arr[i+2] if arr[i+2] > arr[i+1] else arr[i+1])  # 오른쪽 두 건물 중 더 높은 건물로 계산
        if left_side > 0 and right_side > 0:  # 둘 다 값이 0보다 크다면
            view_sum += left_side if left_side <= right_side else right_side  # 더 낮은 값을 더함
    print(f'#{t} {view_sum}')
