import sys
sys.stdin = open('input_20728.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 총 주머니의 수 N, 나눠줄 주머니의 수 K
    N, K = map(int, input().split())
    # 각 주머니의 사탕 수, 내림차순 정렬을 통해 차이를 구해야할 값들을 설정 가능
    candy_list = sorted(list(map(int, input().split())), reverse=True)
    # 초기 값 : 가장 큰 값과 차이가 가장 작을 때의 값(나눠줘야할 사탕 수의 최솟값 중 가장 큰값이 K-1번째)
    answer = candy_list[0] - candy_list[K-1]
    # 반복을 통해 각 값별 차이 구하기
    for i in range(N-K+1):
        temp = candy_list[i] - candy_list[i+K-1] 
        # 최솟값을 구하기 위한 비교식
        if answer > temp:
            answer = temp
    print(f'#{t} {answer}')