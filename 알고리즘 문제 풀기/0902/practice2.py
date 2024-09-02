# 0 1 2 3 4 5 5 4 3 2 1 0을 재귀호출을 이용하여 구현한다.
def rec_print(v):
    if v == N:
        return
    print(v, end=" ")
    rec_print(v + 1)
    print(v, end=" ")


N = int(input())
rec_print(0)
print()
