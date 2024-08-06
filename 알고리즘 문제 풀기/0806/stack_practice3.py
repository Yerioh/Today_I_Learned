a = 10
b = 20


def f1(b, a):
    print("start f1")
    c = a + b
    d = a - b
    print(f2(c, d))
    print("end f1")


def f2(c, d):
    print("start f2")
    c = 1
    d = 2
    print("end f2")
    return c + d


f1(a, b)

# start f1
# start f2
# end f2
# 3
# end f1
