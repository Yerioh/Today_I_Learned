import sys
sys.stdin = open("input_1948.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    date_list = list(map(int, input().split()))

    # 월별 날짜
    # 1월의 경우 일자만 계산하면 되기 때문에 0추가
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date_1 = sum(month[:date_list[0]]) + date_list[1]
    date_2 = sum(month[:date_list[2]]) + date_list[3]

    print(f'#{t} {date_2 - date_1 + 1}')