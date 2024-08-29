import sys

sys.stdin = open("txt/in_15230.txt", "r")

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    my_str = input()  # 입력받은 문자열
    n = len(my_str)  # 입력받은 문자열의 길이
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # 검증을 위한 문자열
    answer = 0  # 순서에 맞게 적혀있는 알파벳의 개수
    for i in range(n):
        if my_str[i] != alphabet[i]:  # 다른 알파벳을 만나면 종료
            break
        answer += 1
    print(f"#{tc} {answer}")
