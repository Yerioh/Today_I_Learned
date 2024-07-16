import sys
sys.stdin = open("swea_1983.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 학생의 수 N, 성적을 알고 싶은 학생의 번호 K
    N, K = map(int, input().split())
    # 성적 딕셔너리
    score_dict = {0:'A+', 1:'A0', 2:'A-', 3:'B+', 4:'B0', 5:'B-', 6:'C+', 7:'C0', 8:'C-', 9:'D0'}
    # 학생 번호, 성적 리스트
    stu_score = []
    for i in range(1, N+1): 
        # 성적 리스트 추가
        li = list(map(int, input().split()))
        # 성적 합산 점수로 리스트 추가
        stu_score.append([i, round(li[0]*0.35 + li[1]*0.45 + li[2]*0.2, 4)])
    stu_score = sorted(stu_score, key=lambda x: -x[1])
    # 리스트 인덱스 참조 위한 카운트
    count = 0
    for i in range(10):
        for j in range(int(N/10)):
            stu_score[count][1] = score_dict[i]
            count += 1
    print(f'#{t} {dict(stu_score)[K]}')

        