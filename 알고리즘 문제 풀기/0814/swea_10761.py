import sys

sys.stdin = open("txt/in_10761.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = input().split()
    N, lst = int(arr[0]), arr[1:]  # 버튼의 개수 N, 버튼 쌍
    # 각 자 눌러야할 버튼
    blue_btn = []
    orange_btn = []
    player = []
    for i in range(N):
        player.append(lst[i * 2])
        if lst[i * 2] == "B":
            blue_btn.append(int(lst[i * 2 + 1]))
        if lst[i * 2] == "O":
            orange_btn.append(int(lst[i * 2 + 1]))
    blue = orange = 1  # 블루와 오렌지의 현재 위치
    answer = 0
    while player:
        answer += 1
        turn = player[0]
        # 블루 차례일 때
        if turn == "B":
            # 블루가 취할 행동
            if blue > blue_btn[0]:
                blue -= 1
            elif blue < blue_btn[0]:
                blue += 1
            else:
                blue_btn.pop(0)
                player.pop(0)
            # 오렌지가 취할 행동
            if orange_btn:  # 오렌지가 행동할 이유가 있다면
                if orange > orange_btn[0]:
                    orange -= 1
                elif orange < orange_btn[0]:
                    orange += 1
        # 오렌지 차례일 때
        if turn == "O":
            # 오렌지가 취할 행동
            if orange > orange_btn[0]:
                orange -= 1
            elif orange < orange_btn[0]:
                orange += 1
            else:
                orange_btn.pop(0)
                player.pop(0)
            # 블루가 취할 행동
            if blue_btn:  # 블루가 행동할 이유가 있다면
                if blue > blue_btn[0]:
                    blue -= 1
                elif blue < blue_btn[0]:
                    blue += 1
    print(f"#{tc} {answer}")
