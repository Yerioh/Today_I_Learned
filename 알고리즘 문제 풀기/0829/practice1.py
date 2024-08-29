"""
0000000111100000011000000111100110000110000111100111100111111001100111
"""
bin_numbers = input()
n = len(bin_numbers) // 7
bin_list = [''] * n  # 2진수를 7개씩 나누어 담을 리스트
for i in range(n):
    bin_list[i] = bin_numbers[i * 7: (i + 1) * 7]
answer = [0] * n  # 2진수를 10진수로 바꾸어 담을 리스트
for i in range(n):
    dec_num = 0
    bin_num = bin_list[i]
    # 2 ** 0 ~ 6까지를 2진수의 뒤부터 곱해주면 변환
    for j in range(7):
        dec_num += (2 ** j) * int(bin_num[6 - j])
    answer[i] = dec_num
print(f"#", *answer)
