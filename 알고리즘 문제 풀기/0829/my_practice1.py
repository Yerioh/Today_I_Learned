def dec_to_bin(n):
    bin_num = ""
    if n == 0:
        return "0"
    while n > 0:
        bin_num = str(n % 2) + bin_num
        n //= 2
    return bin_num


def dec_to_hex(n):
    hex_num = ""
    hex_code = "0123456789ABCDEF"
    if n == 0:
        return "0"
    while n > 0:
        hex_num = hex_code[n % 16] + hex_num
        n //= 16
    return hex_num


my_num = 26
print(dec_to_bin(my_num))
print(dec_to_hex(my_num))
