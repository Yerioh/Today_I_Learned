import sys
sys.stdin = open('input_hw1.txt', 'r')

T = 10  # 테스트 케이스의 수
for t in range(1, T+1):
    N = int(input())  # 최대 덤프 횟수
    boxes = list(map(int, input().split()))  # 박스 배열
    for _ in range(N):
        max_box = 0  # 가장 높은 상자의 크기
        max_box_idx = 0  # 가장 높은 상자의 위치
        min_box = 1001  # 가장 낮은 상자의 크기
        min_box_idx = 0  # 가장 낮은 상자의 위치
        for i in range(100):
            # 가장 높은 상자 찾기
            if boxes[i] > max_box:
                max_box = boxes[i]
                max_box_idx = i
            # 가장 낮은 상자 찾기
            if boxes[i] < min_box:
                min_box = boxes[i]
                min_box_idx = i
        boxes[max_box_idx] -= 1
        boxes[min_box_idx] += 1

    max_box = 0  # 가장 높은 상자의 크기
    min_box = 1001  # 가장 낮은 상자의 크기
    for i in range(100):
        # 가장 높은 상자 찾기
        if boxes[i] > max_box:
            max_box = boxes[i]
            max_box_idx = i
        # 가장 낮은 상자 찾기
        if boxes[i] < min_box:
            min_box = boxes[i]
            min_box_idx = i
    print(f'#{t} {max_box - min_box}')
