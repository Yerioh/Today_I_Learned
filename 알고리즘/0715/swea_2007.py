import sys
sys.stdin = open("swea_2007.txt", "r")

# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.
# 테스트 케이스의 수
T = int(input())
for t in range(1,T+1):
    # 입력받은 문자열
    str_p = input()
    answer = 0
    # 문자열 길이만큼 반복
    for i in range(len(str_p)):
        # 마디수 계산
        answer += 1
        # 마디와 다음 마디 비교
        if str_p[:i+1] == str_p[i+1:(i+1)*2]:
            break
            
    print(f"#{t} {answer}")