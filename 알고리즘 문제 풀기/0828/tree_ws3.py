import sys

sys.stdin = open("txt/in_ws3.txt", "r")


def check(h):
    # 1 ~ h까지 순회하여 각 단계가 대칭인지 확인
    for i in range(1, h + 1):
        first = 2 ** i  # 각 높이의 첫 값 인덱스
        last = 2 ** (i + 1) - 1  # 각 높이의 마지막 값 인덱스
        for j in range(2 ** (i - 1)):
            # 밖에서 안으로 순회하며 값 비교x
            if arr[first + j] != arr[last - j]:
                return False
    return True


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 트리의 크기 N
    arr = [0] + list(map(int, input().split()))  # 이진 트리 배열
    # H = 0  # 이진 트리의 높이
    # while 2 ** (H + 1) - 1 != N:
    #     H += 1
    H = len(bin(N)[2:]) - 1
    answer = check(H)
    print(f"#{tc} {answer}")



