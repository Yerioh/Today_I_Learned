import sys

sys.stdin = open("txt/in_11445.txt", "r")

T = int(input())  # 테스트 케이스의 수
answer = [""] * T
for tc in range(T):
    # 입력받은 두 문자열
    P, Q = input().split()[0], input().split()[0]
    result = "Y"
    # P의 길이가 10이하 일 때, P에 a를 더한것이 Q라면 사이에 다른 단어는 없다
    # len(P) < 10: 이것도 빼야 맞네..
    if P + "a" == Q:
        result = "N"
    # 이 부분 때문에 1개 틀렸는데 왜 틀린건지 모름
    # # P의 길이가 10이면 Q의 길이도 10,
    # # 9번째 글자까지 같고 마지막 단어가 하나차이 나면 다른 단어 없다
    # if len(P) == 10 and P[:9] == Q[:9] and ord(Q[9]) == ord(P[9]) + 1:
    #     result = "N"
    answer[tc] = f"#{tc + 1} {result}"
print(*answer, sep="\n")
