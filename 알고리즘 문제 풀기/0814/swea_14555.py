import sys

sys.stdin = open("txt/in_14555.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    arr = list(input())
    answer = 0
    i = 0
    while i < len(arr):
        if arr[i] == "(":
            if arr[i + 1] in ")|":
                answer += 1
                i += 1
        elif arr[i] == "|":
            if i + 1 < len(arr) and arr[i + 1] == ")":
                answer += 1
                i += 1
        i += 1
    print(f"#{tc} {answer}")
