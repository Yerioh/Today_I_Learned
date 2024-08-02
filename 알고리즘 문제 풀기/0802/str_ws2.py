import sys

sys.stdin = open('txt/input_ws2.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = input()  # 문자열 N
    M = input()  # 문자열 M
    char_dict = {}
    for char1 in N:
        # char1이 char_dict 에 없을 만 실행
        if char1 not in char_dict.keys():
            for char2 in M:
                if char1 == char2:
                    if char1 in char_dict.keys():
                        char_dict[char1] += 1
                    else:
                        char_dict[char1] = 1
    answer = 0
    for key in char_dict:
        if answer < char_dict[key]:
            answer = char_dict[key]
    print(f'#{tc} {answer}')
