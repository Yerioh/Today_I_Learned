import sys
sys.stdin = open("swea_1859.txt", "r")
### 해당 문제는 리스트를 앞에서부터 참조할 경우 런타임 에러가 걸리기 때문에 뒤에서부터 참조하록 알고리즘을 짜야함
# 테스트 케이스 수
T = int(input())
for t in range(1,T+1):
    # 미래를 본 날짜의 수, 정수 n
    n = int(input())
    # 각 날짜별 가격 리스트
    li = list(map(int, input().split()))
    # 판매가 초기화(리스트의 마지막 값)
    sell = li[-1]
    # 정답 초기화
    answer = 0
    # 리스트의 뒤에서부터 참조하도록 반복문 작성
    for i in range(n-1, -1, -1):
        buy = li[i]
        if sell > buy : # 판매가능시 가격 누적
            answer += (sell - buy)
        else: # 판매 불가능시 판매가 변경
            sell = buy
    print(f'#{t} {answer}')