def encoding(n):
    return n ^ 1004


def decoding(n):
    return n ^ 1004


N = int(input())
print("입력받은 수: ", N)
print("암호화: ", encoding(N))
print("복호화: ", decoding(encoding(N)))
