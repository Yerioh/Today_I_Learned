import sys
sys.stdin = open("swea_1966.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 숫자열의 길이
    N = int(input())

    # 입력받은 숫자열
    num_list = list(map(int, input().split()))

    print(f'#{t} {" ".join(list(map(str, sorted(num_list))))}')