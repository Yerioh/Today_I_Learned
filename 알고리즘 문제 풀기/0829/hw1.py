import sys

sys.stdin = open("txt/in_hw1.txt", "r")


decoding_pattern = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}


def get_secret_code(arr):
    # 배열을 순회하여 암호문 찾기
    for r in range(N):
        for c in range(M - 1, -1, -1):
            # 뒤에서 가장 먼저 찾은 1이 암호문의 마지막
            if arr[r][c] == "1":
                return arr[r][c - 55:c + 1]
    return "Not Found"


def decoding(code):
    if code == "Not Found":
        return "Error"
    decode_list = [0] * 8
    # 56글자를 7개씩 끊어 8번 복호화
    for i in range(8):
        temp = code[i * 7: (i + 1) * 7]
        decode_list[i] = decoding_pattern[temp]
    result = 0
    check = 0
    for i in range(8):
        result += decode_list[i]
        if not i % 2:  # 홀수번째면(짝수 인덱스)
            check += decode_list[i] * 3
        else:  # 짝수번째면(홀수 인덱스)
            check += decode_list[i]
    if check % 10:  # 검증 값이 10의 배수가 아니라면
        return 0
    return result


T = int(input())  # 테스트케이스의 수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열의 크기
    arr = [input() for _ in range(N)]  # 암호문이 숨어있는 배열
    secret_code = get_secret_code(arr)
    answer = decoding(secret_code)
    print(f"#{tc} {answer}")
