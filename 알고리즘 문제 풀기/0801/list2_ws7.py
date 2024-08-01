import sys

sys.stdin = open('txt/input_ws7.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 당근의 개수
    C = list(map(int, input().split()))  # 당근의 크기 리스트

    max_cnt = 0  # 카운트의 최대 값
    cnt = 1  # 연속으로 커지는 당근의 크기 카운트
    for i in range(1, len(C)):
        if C[i] > C[i-1]:  # 커졌다면 cnt 증가
            cnt += 1
        else:  # 커지지 않았다면 cnt 초기화
            cnt = 1
        # max_cnt 갱신
        if cnt > max_cnt:
            max_cnt = cnt
    print(f'#{tc} {max_cnt}')
