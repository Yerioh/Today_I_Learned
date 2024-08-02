import sys

sys.stdin = open('txt/input_hw1.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for _ in range(T):
    tc, N = input().split()
    gns = input().split()
    n = int(N)
    # 각 숫자의 갯수를 담을 딕셔너리
    num_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    for i in range(n):
        num_dict[gns[i]] += 1
    # 정답 정렬 하기
    answer = []
    for key in num_dict:
        for i in range(num_dict[key]):
            answer.append(key)
    print(tc, *answer)
