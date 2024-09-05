"""
4
10
11
50
81

#1 Yes
#2 No
#3 No
#4 Yes
"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    answer = "No"
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                answer = "Yes"
                break
        if answer == "Yes":
            break
    print(f"#{tc} {answer}")
