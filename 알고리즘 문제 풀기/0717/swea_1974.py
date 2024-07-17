import sys
sys.stdin = open("swea_1974.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 스도쿠 퍼즐 입력
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # 답변 초기화
    answer = 1

    # 행 탐색
    for i in range(9):
        if len(set(sudoku[i])) != 9:
            answer = 0
    # 열 탐색
    for i in range(9):
        cal_list = list(map(lambda x : x[i], sudoku))
        if len(set(cal_list)) != 9:
            answer = 0
    # 3x3 탐색
    for i in range(3):
        for j in range(3):
            li1, li2, li3 = [[sudoku[i*3+k][j*3], sudoku[i*3+k][j*3+1], sudoku[i*3+k][j*3+2]] for k in range(3)]
            square_list = li1 + li2 + li3
            if len(set(square_list)) != 9:
                answer = 0

    print(f'#{t} {answer}')