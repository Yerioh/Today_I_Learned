def my_push(item, size):
    global top
    top += 1
    if top == size:
        top -= 1  # overflow 시 top 값을 이전 값으로 되돌림
        print('overflow')
    else:
        stack[top] = item


def my_pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]


N = 10
stack = [0] * N
top = -1

for i in range(1, 12):
    my_push(i, N)
    print(stack, top)

for _ in range(11):
    print(my_pop(), top)

