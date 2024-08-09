lst = [1, 2, 3, 4, 5]

N = 5

cnt = 0


# 현재 수를 고려하고 있는 위치,
# 순열을 만들 때 이전에 사용했던 원소 체크,
# 지금까지 만든 순열 ,
# 순열의 길이
def make_perm(idx, selected, result, n):
    global cnt
    cnt += 1
    # 종료 조건
    if idx == n:
        # 지금까지 만든 순열 출력
        print(result)
        return
    # 재귀 호출
    for i in range(n):
        # 현재 고른 적 없는 원소를 넣음
        if not selected[i]:
            selected[i] = 1
            result.append(lst[i])
            # idx + 1 번째 자리 정하기
            make_perm(idx + 1, selected, result, n)

            # 다른 원소를 고르기 위한 경우
            selected[i] = 0
            result.pop()


make_perm(0, [0] * N, [], N)
print('함수 실행 횟수:', cnt)
