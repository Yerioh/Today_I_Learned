import sys
sys.stdin = open("swea_1970.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 거스름돈 N
    N = int(input())

    # 각 화폐의 수 리스트 초기화(5만원 -> 10원)
    change_list = []

    # 화폐 딕셔너리
    money_dict = {0:50000, 1:10000, 2:5000, 3:1000, 4:500, 5:100, 6:50, 7:10}

    for i in range(8):
        change_list.append(str(N//money_dict[i]))
        N %= money_dict[i]
    print(f'#{t}\n{" ".join(change_list)}')
    