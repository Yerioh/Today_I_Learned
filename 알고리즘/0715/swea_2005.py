import sys
sys.stdin = open("swea_2005.txt", "r")

# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
# 테스트 케이스의 수
T = int(input())
for t in range(1,T+1):
    # 정수 N
    N = int(input())
    num_list = []
    for i in range(N): # N만큼 반복
        if i == 0: # 처음엔 [1]
            num_list.append(["1"])
        else: # 이후부턴 앞 리스트 참조
            li = []
            for j in range(i+1):
                if j==0: # 처음은 1
                    li.append(1)
                elif j==i: # 마지막은 1
                    li.append(1)
                else: # 처음과 마지막이 아니면 인덱스 활용하여 값 참조
                    li.append(num_list[i-1][j-1]+num_list[i-1][j])
            num_list.append(li)
    print(f"#{t}")
    for i in range(N):
        print(" ".join(list(map(str, num_list[i]))))