"""
3
3
1 2 3
5
1 1 1 3 3
8
1 2 3 4 5 6 7 8

"""


def select_box(lev):
    global result
    if lev == N:
        small = carrot_box.count(0)  # 소 박스의 당근 수
        middle = carrot_box.count(1)  # 중 박스의 당근 수
        big = carrot_box.count(2)  # 대 박스의 당근 수
        if middle > 0 and big > 0:
            temp = max(small, middle, big) - min(small, middle, big)
            result = min(result, temp)
        return
    if carrot[lev] == carrot[lev - 1]:  # 현재 당근이 앞 당근과 같다면
        carrot_box[lev] = carrot_box[lev - 1]
        select_box(lev + 1)
    else:
        if not carrot_box.count(1):  # 중 박스에 넣은 것이 없을 때만
            carrot_box[lev] = 0
            select_box(lev + 1)
        carrot_box[lev] = 1
        select_box(lev + 1)
        if carrot_box.count(1) > 0:  # 대 박스는 중박스에 넣은 것이 있을 때만
            carrot_box[lev] = 2
            select_box(lev + 1)


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 당근의 개수
    carrot = sorted(list(map(int, input().split())))  # 각 당근의 무게
    result = -1
    if len(set(carrot)) >= 3:
        result = 1000
        carrot_kg = [0] * 31
        for i in range(N):
            carrot_kg[carrot[i]] += 1
        carrot_box = [0] * 3  # 0 : 소, 1 : 중, 2 : 대
        carrot_box[0] += 1  # 가장 작은 당근은 맨 앞에
        select_box(1)
    print(f"#{tc} {result}")
