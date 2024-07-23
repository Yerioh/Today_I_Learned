import sys
sys.stdin = open('input_20019.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1,T+1):
    # 입력받은 문자열
    S = input()
    answer ="YES"
    if S[:len(S)//2 ] != S[len(S)//2 + 1:][::-1]:
        answer ="NO"

    if answer == "YES":
        # 회문의 회문의 경우 길이가 짝수일때도 생각해야함
        s = S[:len(S)//2]
        if len(s)%2:
            if s[:len(s)//2] != s[len(s)//2 + 1:][::-1]:
                answer = "NO"
        else:
            if s[:len(s)//2] != s[len(s)//2:][::-1]:
                answer = "NO"
    print(f'#{t} {answer}')