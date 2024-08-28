import sys

sys.stdin = open("txt/in_15868.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 두 수열 및 배열의 크기
    arr = [list(map(int, input())) for _ in range(N)]  # XOR 을 확인할 배열
    lst_n = [-1] * N
    lst_n[0] = 0  # 임의로 n 수열의 첫 값은 0으로
    lst_m = [-1] * M
    answer = "yes"
    for i in range(N):
        for j in range(M): 
            if lst_n[i] >= 0 and lst_m[j] >= 0:  # 둘 다 값을 알 때
                # 배열의 값이 1이지만, 두 수가 같다면 성립 불가능
                if arr[i][j] and lst_n[i] == lst_m[j]:  
                    answer = "no"
                # 배열의 값이 0이지만, 두 수가 다르면 성립 불가능
                if not arr[i][j] and lst_n[i] != lst_m[j]:
                    answer = "no"
            else:  # 둘 중 하나라도 값을 모를 때
                if lst_n[i] >= 0:  #  n 수열의 값을 알 때
                    if arr[i][j]:  # 두 수의 값이 다를 때
                        lst_m[j] = 0 if lst_n[i] else 1
                    else:
                        lst_m[j] = 1 if lst_n[i] else 0
                elif lst_m[j] >= 0:  # m 수열으 값을 알 때
                    if arr[i][j]:  # 두 수의 값이 다를 때
                        lst_n[i] = 0 if lst_m[j] else 1
                    else:
                        lst_n[i] = 1 if lst_m[j] else 0
    print(f"#{tc} {answer}")
