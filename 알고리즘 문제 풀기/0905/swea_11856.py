"""
5
ABAB
CCDD
EFFE
EEEE
NONE

#1 Yes
#2 Yes
#3 Yes
#4 No
#5 No
"""

T = int(input())
for tc in range(1, T + 1):
    S = input()
    cnt_dict = {}
    for s in S:
        if s in cnt_dict.keys():
            cnt_dict[s] += 1
        else:
            cnt_dict[s] = 1
    answer = "Yes"
    if len(cnt_dict) != 2:
        answer = "No"
    else:
        for key in cnt_dict:
            if cnt_dict[key] != 2:
                answer = "No"
    print(f"#{tc} {answer}")
