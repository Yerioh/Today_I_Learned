"""
3
4 47FE
5 79E12
8 41DA16CD

"""

T = int(input())
for tc in range(1, T + 1):
    N, hex_num = input().split()
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
    answer = ""
    for char in hex_num:
        answer += hex_bin_dict[char]
    print(f"#{tc} {answer}")
