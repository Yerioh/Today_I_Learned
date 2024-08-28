import sys

sys.stdin = open("txt/in_ws2.txt", "r")


def search_node_value(num):
    s = arr[num]
    # 재귀 함수를 사용해 단말노드에 접근해 값을 가져와 더하기
    if num * 2 + 1 <= N:  # 오른쪽 자식 노드가  있다면
        s += search_node_value(num * 2 + 1)
    if num * 2 <= N:  # 왼쪽 자식 노드가 있다면
        s += search_node_value(num * 2)
    return s


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    # 노드의 개수, 리프 노드의 개수, 출력할 노드 번호
    N, M, L = map(int, input().split())
    arr = [0] * (N + 1)  # N개의 노드를 가지고 있는 완전 이진 트리
    for _ in range(M):
        node, key = map(int, input().split())
        arr[node] = key
    answer = search_node_value(L)
    print(f"#{tc} {answer}")
