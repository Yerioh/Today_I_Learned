# 3개의 주사위를 던져 나올 수 있는 중복 순열에 대해,
# 합이 10 이하가 나오는 경우는 총 몇가지인가?

def dice_sum(v, s):
    global answer
    if s > 10:
        return
    if v == 3:
        if s <= 10:
            answer += 1
        return
    for i in range(1, 7):
        result[v] = i
        dice_sum(v + 1, s + i)


answer = 0
result = [0] * 3
dice_sum(0, 0)
print("합이 10이가 나오는 경우의 수:", answer)
