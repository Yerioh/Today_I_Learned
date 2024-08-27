'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


# 전위 순회
def pre_order(T):
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])


# 중위 순회
def in_order(T):
    if T:
        in_order(left[T])
        print(T, end=' ')
        in_order(right[T])


# 후위 순회
def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        print(T, end=' ')


N = int(input())  # 1번부터 N번까지인 정점
E = N - 1
arr = list(map(int, input().split()))
left = [0] * (N + 1)  # 부모를 인덱스로 왼쪽자식번호 저장
right = [0] * (N + 1)  #
par = [0] * (N + 1)  # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    # for i in range(0,E*2, 2):
    #         p, c = arr[i], arr[i + 1]
    if left[p] == 0:  # 왼쪽자식이 없으면
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:  # 부모가 있으면
    c = par[c]  # 부모를 새로운 자식으로 두고
root = c  # 더이상 부모가 없으면 root
print(root)
print('전위 순회 :', end=' ')
pre_order(root)
print()
print('중위 순회 :', end=' ')
in_order(root)
print()
print('후위 순회 :', end=' ')
post_order(root)
