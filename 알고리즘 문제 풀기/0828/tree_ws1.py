import sys

sys.stdin = open("txt/in_ws1.txt", "r")


def my_heap_push(t):
    # 마지막 위치에 삽입
    global last_idx
    last_idx += 1
    min_heap[last_idx] = t
    # 부모 자식 비교
    c = last_idx
    p = c // 2
    # 부모가 있고(루트 노드가 아니고), 부모가 자식보다 크다면
    while p >= 1 and min_heap[p] > min_heap[c]:
        min_heap[p], min_heap[c] = min_heap[c], min_heap[p]
        # 상위와 또 비교하기 위해 값 변경
        c = p
        p = c // 2


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 노드의 수 N
    arr = list(map(int, input().split()))  # 입력받은 숫자들
    # 힙은 완전 이진트리
    min_heap = [0] * (N + 1)
    last_idx = 0  # 힙의 마지막 인덱스
    for num in arr:
        my_heap_push(num)
    # 조상 노드의 합 구하기
    answer = 0
    par_idx = last_idx // 2  # 마지막 노드의 부모 노드 인덱스
    while par_idx >= 1:  # 부모 노드가 있다면
        answer += min_heap[par_idx]
        par_idx //= 2  # 현재 부모 노드의 부모 노드로 변경
    print(f"#{tc} {answer}")
