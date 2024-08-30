"""
3
11
128
2147483645

#1 3
#2 1
#3 30
"""


def dec_to_bin(n):
    temp_bin = ""
    while n > 0:
        temp_bin = str(n % 2) + temp_bin
        n //= 2
    return temp_bin


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    for char in dec_to_bin(N):
        if char == "1":
            answer += 1
    print(f"#{tc} {answer}")
