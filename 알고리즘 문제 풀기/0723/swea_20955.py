import sys
sys.stdin = open('input_20955.txt', 'r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    S = input()
    E = input()

    # S와 E의 길이의 차만큼 반복
    for i in range(len(E)-len(S)):
        if E[-1] == 'X':
            E = E[:-1]
        else:

            E = ''.join([c for c in E[:-1]][::-1])
    print(f"#{t} {'Yes' if S == E else 'No'}")