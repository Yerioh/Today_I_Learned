import sys
sys.stdin = open('input_1945.txt', 'r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    N = int(input())

    num_list = [2, 3, 5, 7, 11]
    answer = []
    for num in num_list:
        count = 0
        while N%num==0:
            N /= num
            count += 1
        answer.append(str(count))
    print(f'#{t} {" ".join(answer)}')