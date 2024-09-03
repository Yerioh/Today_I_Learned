# 반복문으로 조합 구성해보기 (5개 중 3개 뽑기)
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            print(i, j, k)
print("------------")


# 함수로 구현해보기
def get_comb(lev, t):
    if lev == M:
        print(*result)
        return
    for i in range(t, N):
        result[lev] = i
        get_comb(lev + 1, i + 1)


N, M = 5, 3  # 전체 N개 중 M개 고르기
result = [0] * M
get_comb(0, 0)
print("----------------")


# 주사위 고르기
def get_dice_comb(dice, t):
    if dice == 3:
        print(*dice_result)
        return
    for i in range(t, 7):
        dice_result[dice] = i
        get_dice_comb(dice + 1, i)


dice_result = [0] * 3
get_dice_comb(0, 1)
