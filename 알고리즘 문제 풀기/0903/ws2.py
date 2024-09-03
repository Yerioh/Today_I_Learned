import sys

sys.stdin = open("txt/in_ws2.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 컨테이너의 수, 트럭의 수
    container_arr = list(map(int, input().split()))  # 화물의 무게
    truck_arr = list(map(int, input().split()))  # 트럭의 적재용량
    # 화물과 트럭을 내림차순으로 정렬
    container_arr.sort(reverse=True)
    truck_arr.sort(reverse=True)
    answer = 0
    select_container = [0] * N  # 적재한 적이 있는 화물인지 검사
    for truck in truck_arr:
        for i in range(N):
            if truck >= container_arr[i] and not select_container[i]:
                answer += container_arr[i]
                select_container[i] = 1
                break
    print(f"#{tc} {answer}")
