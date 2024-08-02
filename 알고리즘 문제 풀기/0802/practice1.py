# 문자열 뒤집기 for 문 이용하여 구현
def reverse_string(my_str):
    len_s = 0
    for _ in my_str:
        len_s += 1
    new_str = ''
    for i in range(len_s):
        new_str += my_str[len_s - 1 - i]
    return new_str


# 문자열 비교 함수
def str_is_equal(str1, str2):
    len1 = 0
    for _ in str1:
        len1 += 1
    len2 = 0
    for _ in str2:
        len2 += 1
    answer = True
    if len1 == len2:
        for i in range(len1):
            if str1[i] != str2[i]:
                answer = False
        return answer
    else:
        return False


s = 'hello world'
print(reverse_string(s))
print(str_is_equal('hello', 'hello'))
print(str_is_equal('hello', 'world'))
print(str_is_equal('hi', 'hello'))
