lst = [1, 2, 3, 4, 5]

N = 5

cnt = 0


# 다른 자리와 위치를 바꿀지 고민 중인 위치
# 순열의 길이
def make_perm(idx, n):
    global cnt
    cnt += 1
    # 종료 조건
    if idx == n:
        print(lst)
        return
    # 재귀 호출
    # idx == j : 자리를 바꾸지 않겠다.
    for j in range(idx, n):
        lst[idx], lst[j] = lst[j], lst[idx]
        # 다음 위치 구하기
        make_perm(idx + 1, n)
        # 다른 위치와 바꾸는 경우를 위해 순서 복구
        lst[idx], lst[j] = lst[j], lst[idx]


make_perm(0, N)
print('함수 실행 횟수:', cnt)
