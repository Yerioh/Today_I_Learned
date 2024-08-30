import sys

sys.stdin = open("txt/in_hw1.txt", "r")


def hex_to_bin(n):
    hex_bin_dict = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }
    return hex_bin_dict[n]


def check_secret_code(my_code):
    # 인덱스를 통해 코드 복호화
    decoding_pattern = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1], [1, 3, 2],
                        [2, 3, 1], [1, 1, 4], [3, 1, 2], [2, 1, 3], [1, 1, 2]]
    # 비율에 맞게 코드 변환
    for i in range(8):
        min_num = min(my_code[i])
        lst = list(map(lambda x: x // min_num, my_code[i]))
        my_code[i] = lst
    decoding_code = list(map(lambda x: decoding_pattern.index(x), my_code))
    result = 0
    check = 0
    for i in range(8):
        result += decoding_code[i]
        if not i % 2:
            check += decoding_code[i] * 3
        else:
            check += decoding_code[i]
    if check % 10:
        return 0
    return result


T = int(input())  # 테스트케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기
    arr1 = [input()[:M] for _ in range(N)]  # 암호를 담은 배열
    # 0으로 채워져 있는 열에는 암호문이 없다
    arr2 = []
    for r in range(N):
        if int(arr1[r], 16) and arr1[r] not in arr2:
            arr2.append(arr1[r])
    # 암호문 찾기
    secret_code_list = []
    for hex1 in arr2:
        # 해당열을 전부 이진수로 변경
        bin1 = list("".join(list(map(hex_to_bin, hex1))))
        m = M * 4
        temp = [[] for _ in range(8)]  # 코드 뭉치를 찾을 임시 배열
        idx = 0  # 배열의 인덱스
        cnt = 0  # 코드를 찾기 위한 카운트
        code = [0] * 3  # 이 리스트를 다 채우면 코드 하나 찾은것
        for c in range(m):
            if not code[0]:
                if bin1[c] == "1":
                    cnt += 1
                elif cnt and bin1[c] == "0":
                    code[0] = cnt
                    cnt = 1
            elif not code[1]:
                if bin1[c] == "0":
                    cnt += 1
                elif bin1[c] == "1":
                    code[1] = cnt
                    cnt = 1
            elif not code[2]:
                if bin1[c] == "1":
                    cnt += 1
                elif bin1[c] == "0":
                    code[2] = cnt
                    cnt = 0
                    temp[idx] = code
                    idx += 1
                    code = [0] * 3
            if idx == 8:  # 8개의 코드가 하나의 코드 뭉치
                # 찾아낸 코드가 다른 열에서 찾은 코드와 같을 경우는 넣지 않는다.
                if temp not in secret_code_list:
                    secret_code_list.append(temp)
                # 초기화
                idx = 0
                temp = [[] for _ in range(8)]
    answer = 0
    for secret_code in secret_code_list:
        answer += check_secret_code(secret_code)
    print(f"#{tc} {answer}")
