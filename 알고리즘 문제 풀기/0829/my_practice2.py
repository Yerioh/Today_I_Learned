def hex_to_bin(hex_num):
    bin_num = ""
    if hex_num == "0":
        return "0"
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
    n = len(hex_num)
    for i in range(n):
        bin_num += hex_bin_dict[hex_num[i]]
        if i != n - 1:
            bin_num += " "
    return bin_num


my_hex_num = "F3"
print(hex_to_bin(my_hex_num))
