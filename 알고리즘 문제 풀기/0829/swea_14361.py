import sys

sys.stdin = open("txt/in_14361.txt", "r")


def check_sequence_n(my_num, result, selected):
    global answer
    if answer == "possible":  # 이미 배수를 찾았다면
        return
    if len(result) == len(my_num):
        res, num = int(result), int(my_num)
        if res > num and res % num == 0:  # 현재 만들어진 수열이 배수라면
            answer = "possible"
        return
    else:
        for i in range(len(my_num)):
            if not selected[i]:
                result += my_num[i]
                selected[i] = 1
                check_sequence_n(my_num, result, selected)
                result = result[:len(result) - 1]
                selected[i] = 0


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = input()  # 입력받은 정수
    answer = "impossible"
    check_sequence_n(N, "", [0] * len(N))
    print(f"#{tc} {answer}")
