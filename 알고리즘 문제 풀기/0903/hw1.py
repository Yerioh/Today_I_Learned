import sys

sys.stdin = open("txt/in_hw1.txt", "r")


def baby_gin(lev, t, comb, n):
    global answer
    if lev == 3:
        # player1 검사
        if player1_card[comb[0]] == player1_card[comb[1]] == player1_card[comb[2]]:
            answer = 1
            return
        temp1 = sorted([player1_card[comb[0]], player1_card[comb[1]], player1_card[comb[2]]])
        if temp1[2] - temp1[1] == temp1[1] - temp1[0] == 1:
            answer = 1
            return
        # player2 검사
        if player2_card[comb[0]] == player2_card[comb[1]] == player2_card[comb[2]]:
            answer = 2
        temp2 = sorted([player2_card[comb[0]], player2_card[comb[1]], player2_card[comb[2]]])
        if temp2[2] - temp2[1] == temp2[1] - temp2[0] == 1:
            answer = 2
        return
    for i in range(t, n):
        comb[lev] = i
        baby_gin(lev + 1, i + 1, comb, n)


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))  # 카드 리스트
    # 각 카드를 플레이어에 맞게 배분
    player1_card = [0] * 6
    player2_card = [0] * 6
    answer = 0
    for i in range(6):
        player1_card[i], player2_card[i] = arr[i * 2], arr[i * 2 + 1]
        if i >= 2:  # 3장 이상일 때부터 triplet, run 확인
            baby_gin(0, 0, [0] * 3, i + 1)
        # 한명이라도 됐다면 종료
        if answer:
            break
    print(f"#{tc} {answer}")
