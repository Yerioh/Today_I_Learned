import sys
sys.stdin = open('input_1204.txt', 'r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    test_case = int(input())
    # 수학 점수 리스트
    score_list = list(map(int, input().split()))
    score_list.sort()
    # 각 점수별 횟수를 담을 딕셔너리
    score_dict = {}

    # 리스트를 돌아 각 점수별 수를 딕셔너리에 담음
    for score in score_list:
        if score not in score_dict.keys():
            score_dict[score] = 1
        else:
            score_dict[score] += 1

    answer = 0
    current_cnt = 0
    for key in score_dict:
        if current_cnt < score_dict[key]:
            current_cnt = score_dict[key]
            answer = key
        elif current_cnt == score_dict[key]:
            answer = key
    print(f'#{t} {answer}')