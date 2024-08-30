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

# 연습문제2
# 16진수 문자로 이루어진 1차 배열이 주어질 때
# 앞에서부터 7bit 씩 묶어 십진수로 변환하여 출력해보자.
# 0 116 12 7 76 24 58 121 124 103 3
hex1 = "01D06079861D79F99F"
bin1 = "".join(list(map(lambda x: hex_bin_dict[x], hex1)))
n = len(bin1) // 7 + (1 if len(bin1) % 7 else 0)  # 나머지가 있으면 한번 더
answer = [0] * n
for i in range(n):
    seven_bit = bin1[i * 7: (i + 1) * 7]  # 7bit 씩 묶기
    dec = 0  # 십진수로 변환된 값을 담을 변수
    bit_n = len(seven_bit)  # 7bit 씩 묶고 남은 bit 는 길이가 다르다
    for j in range(bit_n):
        dec += int(seven_bit[bit_n - 1 - j]) * (2 ** j)
    answer[i] = dec
print("2번 정답 :", *answer)

# 연습문제3
# 16진수 문자로 이루어진 1차 배열이 주어질 때,
# 왼쪽부터 순차적으로 암호비트 패턴을 찾아 차례대로 출력하시오.
# 암호는 연속되어 있다.
# 1 1 7 8 0
hex2 = "0269FAC9A0"
bin2 = "".join(list(map(lambda x: hex_bin_dict[x], hex2)))
decoding_pattern = ["001101", "010011", "111011", "110001", "100011", "110111", "001011", "111101", "011001", "101111"]
answer2 = []
i = 0
while i < len(bin2):
    temp = bin2[i: i + 6]
    for j in range(10):
        if decoding_pattern[j] == temp:
            answer2.append(j)
            i += 5
    i += 1
print("3번 정답 :", *answer2)
