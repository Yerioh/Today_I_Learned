import sys

sys.stdin = open("txt/in_ws4.txt", "r")
# 이진 탐색


def binary_search(left, right, key, path):
    global answer
    if left > right:  # 검색 범위가 없다면
        return
    mid = left + (right - left) // 2

    if A[mid] == key:  # 두 값이 같으면
        answer += 1
        return
    elif A[mid] > key:  # 검색할 값이 중앙 값보다 작으면
        if path == "l":  # 전에 왼쪽으로 이동해서 검색했다면
            return
        binary_search(left, mid - 1, key, "l")
    else:  # 검색할 값이 중앙 값보다 크다면
        if path == "r":  # 전에 오른쪽으로 이동해서 검색했다면
            return
        binary_search(mid + 1, right, key, "r")


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # A, B의 개수
    A = sorted(list(map(int, input().split())))  # N개의 정수 리스트
    B = list(map(int, input().split()))  # M개의 정수 리스트
    answer = 0
    for b in B:
        binary_search(0, N - 1, b, "")
    print(f"#{tc} {answer}")
