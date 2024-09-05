import sys

sys.stdin = open("txt/in_ws3.txt", "r")


def get_max_score(idx, kcal, score):
    global answer
    if kcal > limit_kcal:
        return
    if idx == N:
        if score > answer:  # 최댓값 교체
            answer = score
        return
    get_max_score(idx + 1, kcal, score)  # 선택하지 않았을 때
    get_max_score(idx + 1, kcal + arr[idx][1], score + arr[idx][0])  # 선택했을 때


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N, limit_kcal = map(int, input().split())  # 재료의 수, 제한 칼로리
    arr = [list(map(int, input().split())) for _ in range(N)]  # 재료별[점수, 칼로리]
    answer = 0
    get_max_score(0, 0, 0)
    print(f"#{tc} {answer}")
