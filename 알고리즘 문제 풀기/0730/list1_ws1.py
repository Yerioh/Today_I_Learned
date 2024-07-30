T = int(input())  # 테스트 케이스의 수
for t in range(1, T+1):
    N = int(input())  # 카드 장수 N
    cards = list(map(int, input()))  # N장의 카드
    counts = [0] * 10  # 각 카드를 count 할 리스트
    # 각 카드를 카운트
    for card in cards:
        counts[card] += 1
    # counts 를 순회하여 장수가 가장 많은 카드 찾기 (가장 큰 값의 인덱스가 해당 카드)
    max_count_number = 0
    max_count = 0
    for i in range(len(counts)):
        if counts[i] >= max_count:
            max_count = counts[i]
            max_count_number = i
    print(f'#{t} {max_count_number} {max_count}')
