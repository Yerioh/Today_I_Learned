import sys
sys.stdin = open('input_1928.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    enc_strs = input()
    encode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    enc_str_list = [enc_strs[i*4:i*4+4] for i in range(int(len(enc_strs)/4))]

    answer = []

    for enc_str in enc_str_list:
        # 각 구간의 문자를 encode 문자열의 인덱스를 이용하여 숫자로 바꾸고 6자리의 2진수 문자열로 변경하여 리스트에 담기
        idx_list = [('0'*(6-len(bin(encode.index(char))[2:])))+bin(encode.index(char))[2:] for char in enc_str]
        # 2진수 리스트를 하나의 문자열로 합치기
        dec_num = ''.join(idx_list)
        # 합쳐진 2진수 문자열을 각각 8자리의 2진수로 나누고 각 2진수를 10진수로 변경 후 아스키 코드를 이용해 문자열로 변경
        dec_list = [chr(int('0b'+dec_num[i*8: i*8+8], 2)) for i in range(3)]
        answer.append("".join(dec_list))
    print(f'#{t} {"".join(answer)}')