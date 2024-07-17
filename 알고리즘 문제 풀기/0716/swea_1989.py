import sys
sys.stdin = open("swea_1989.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 입력받은 문자열
    s = input()
    # 정답 초기화
    answer = 1
    # 문자열 길이의 절반만큼 반복
    for i in range(len(s)//2):
        # 비교하여 다르다면 답 0으로 바꾸고 break
        if s[i] != s[(i+1)*(-1)]:
            answer = 0
            break
    print(f'#{t} {answer}')