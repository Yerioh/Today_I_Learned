import sys
sys.stdin = open('input_1288.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    N = int(input())

    count = 0

    num_list = []
    while num_list != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        count += 1
        ship = [int(char) for char in str(count*N)]
        for num in ship:
            num_list.append(num)
        num_list = sorted(list(set(num_list)))
    print(f'#{t} {count*N}')