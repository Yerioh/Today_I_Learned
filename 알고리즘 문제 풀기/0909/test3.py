"""
3
3
1 2 3
5
1 1 1 3 3
8
1 2 3 4 5 6 7 8

"""
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 당근의 개수
    carrot = list(map(int, input().split()))  # 각 당근의 무게
    result = -1
    carrot_kind = sorted(list(set(carrot)))  # 당근의 무게 종류
    if len(carrot_kind) >= 3:
        result = 1000
        carrot_weight_cnt = {}  # 무게별 당근 수
        for c in carrot_kind:
            carrot_weight_cnt[c] = carrot.count(c)
        carrot_box = [0] * 3 # 0 : 소, 1 : 중, 2 : 대
        for i in range(len(carrot_kind) - 2):  # 뒤 2개는 남겨두기
            carrot_box[0] += carrot_weight_cnt[carrot_kind[i]]
            carrot_box[1] = 0 # 다음 비교를 위해 초기화
            for j in range(i + 1, len(carrot_kind) - 1): # 뒤 1개는 남겨두기
                carrot_box[1] += carrot_weight_cnt[carrot_kind[j]]
                carrot_box[2] = 0  # 다음 비교를 위해 초기화
                for k in range(j + 1, len(carrot_kind)):
                    carrot_box[2] += carrot_weight_cnt[carrot_kind[k]]
                temp = max(carrot_box) - min(carrot_box)
                result = min(result, temp)
    print(f"#{tc} {result}")
