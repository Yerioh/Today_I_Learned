import sys

sys.stdin = open("txt/in_hw1.txt", "r")


def baby_gin():
    global answer
    for i in range(6):
        # player1 부터 시작
        player1_card = arr[i * 2]
        player1[player1_card] += 1  # 뽑은 카드 수 증가
        if player1[player1_card] == 3:  # 현재 뽑은 카드로 triplet 이 된다면
            answer = 1
            return
        for j in range(player1_card - 1, player1_card + 2):
            # 인덱스 확인, 연속된 카드 확인
            if 1 <= j < 9 and player1[j - 1] and player1[j] and player1[j + 1]:
                answer = 1
                return
        # player2 턴
        player2_card = arr[i * 2 + 1]
        player2[player2_card] += 1  # 뽑은 카드 수 증가
        if player2[player2_card] == 3:  # 현재 뽑은 카드로 triplet 이 된다면
            answer = 2
            return
        for j in range(player2_card - 1, player2_card + 2):
            # 인덱스 확인, 연속된 카드 확인
            if 1 <= j < 9 and player2[j - 1] and player2[j] and player2[j + 1]:
                answer = 2
                return


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))  # 카드 리스트
    # 각 카드를 플레이어에 맞게 배분
    player1 = [0] * 10
    player2 = [0] * 10
    answer = 0
    baby_gin()
    print(f"#{tc} {answer}")
