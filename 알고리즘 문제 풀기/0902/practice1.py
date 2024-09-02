# 1 1 ~ 3 3 까지 출력하는 프로그램을 작성하시오.(반복문 이용)
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


# 1 1 1 1 ~ 3 3 3 3까지 출력하는 코드를 작성하시오.
def print_for(v, result):
    if v == N:
        print(*result)
        return
    for num in range(1, 4):
        result[v] = num
        print_for(v + 1, result)


N = int(input())
print_for(0, [0] * N)
