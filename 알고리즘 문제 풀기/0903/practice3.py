# 화장실 문제
# 대기 시간 누적합의 최소값
arr = [15, 30, 50, 10]
answer = 0
arr.sort()
for i in range(4):
    answer += arr[i] * (3 - i)
print("최소 대기 시간:", answer)


# 0-1 Knapsack
# 어떻게 물건을 잡아야 최대로 수익을 낼 수 있나
N = 3
arr = [(5, 50), (10, 60), (20, 140)]
answer = 0
for i in range(1 << N):
    kg = 0
    price = 0
    for j in range(N):
        if i & (1 << j):
            kg += arr[j][0]
            price += arr[j][1]
    if kg <= 30 and price > answer:
        answer = price
print("최대 수익:", answer)


# 회의실 배정
arr = [(0, 5), (1, 3), (2, 7), (3, 5), (6, 8), (7, 8)]
arr.sort(key=lambda x: x[1])
answer = 1
end_time = arr[0][1]
for i in range(1, 6):
    if arr[i][0] >= end_time:
        answer += 1
        end_time = arr[i][1]
print("최대 회의 수:", answer)
