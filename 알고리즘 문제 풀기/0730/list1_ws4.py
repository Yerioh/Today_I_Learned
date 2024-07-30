import sys

sys.stdin = open('input_ws4.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for _ in range(T):
    t = int(input())  # 테스트 케이스의 번호
    scores = list(map(int, input().split()))  # 점수 리스트
    counts = [0] * 101  # 0~100 까지의 카운트
    for score in scores:  # 점수별 카운트
        counts[score] += 1
    max_count = 0
    max_count_score = 0
    for i in range(101):
        if counts[i] >= max_count:  # 카운트가 가장 큰 값 찾기
            max_count = counts[i]
            max_count_score = i
    print(f'#{t} {max_count_score}')
