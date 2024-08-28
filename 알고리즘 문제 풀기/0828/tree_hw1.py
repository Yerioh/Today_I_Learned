import sys

sys.stdin = open("txt/in_hw1.txt", "r")


def post_order(t):
    if t:  # 후위 순회
        left = post_order(lc[t])
        right = post_order(rc[t])
        if arr[t] not in operator:
            return arr[t]
        else:  # 연산자라면 left right 순으로 계산
            if arr[t] == "+":
                return left + right
            elif arr[t] == "-":
                return left - right
            elif arr[t] == "*":
                return left * right
            elif arr[t] == "/":
                return left / right


for tc in range(1, 11):
    N = int(input())  # 정점의 개수
    # 입력 받은 정점의 정보로 트리 구성
    arr = [0] * (N + 1)
    lc = [0] * (N + 1)  # 왼쪽 자식 노드
    rc = [0] * (N + 1)  # 오른쪽 자식 노드
    operator = ["+", "-", "*", "/"]
    for _ in range(N):
        temp = list(map(lambda x: x if x in operator else int(x), input().split()))
        arr[temp[0]] = temp[1]
        if temp[1] in operator:  # 해당 정점의 값이 연산자라면
            lc[temp[0]], rc[temp[0]] = temp[2], temp[3]
    answer = int(post_order(1))  # 소수점 아래는 버리기
    print(f"#{tc} {answer}")
