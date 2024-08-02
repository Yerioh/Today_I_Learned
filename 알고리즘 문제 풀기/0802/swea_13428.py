import sys

sys.stdin = open('txt/input_13428.txt', 'r')


def max_sort(lst):
    L = len(lst)
    new_lst = lst[:]
    for i in range(L - 1):  # 현재 위치
        if lst[i] != max(lst[i:]):  # 현재 위치 기준 가장 큰 값이 아니면
            max_idx = i
            for j in range(i, L):
                if lst[j] >= lst[i:][max_idx - i]:  # 가장 큰 수 인덱스 찾기
                    max_idx = j
            new_lst[i], new_lst[max_idx] = new_lst[max_idx], new_lst[i]
            return new_lst
    return lst


def min_sort(lst):
    L = len(lst)
    new_lst = lst[:]
    for i in range(L - 1):  # 현재 위치
        if lst[i] != min(lst[i:]):  # 현재 위치 기준 가장 작은 값이 아니면
            min_idx = i
            min_num = 999999
            if i == 0 and min(lst) == 0:

            for j in range(i, L):
                if lst[j] <= lst[i:][min_idx - i]:  # 가장 작은 수 인덱스 찾기
                    min_idx = j
            if i == 0 and lst[min_idx] == 0:  # 맨 앞은 0이 올 수 없다
                pass
            else:
                new_lst[i], new_lst[min_idx] = new_lst[min_idx], new_lst[i]
                return new_lst
    return lst


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T+1):
    N = list(map(int, input()))  # 입력받은 정수를 리스트로
    max_num = "".join(list(map(str, max_sort(N))))
    min_num = "".join(list(map(str, min_sort(N))))
    print(f'#{tc} {min_num} {max_num}')
