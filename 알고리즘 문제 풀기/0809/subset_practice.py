# 부분 집합 만들기, 부분집합의 합 이용한 가지치기
lst = [1, 2, 3, 4, 5]

N = 5

S = 10
print(lst)


# 부분집합을 만드는 함수
# 현재 고려중인 원소의 인덱스, 내가 고른 원소 체크, 원소의 전체 개수
def make_subset(idx, selected, n, s):

    # 가지치기 - 답이 될 가능성이 없으면 더 이상 진행하지 않음
    if s > S:
        return
    # 종료 조건
    # n번 시행 => 부분 집합 구하기 완료
    if idx == n:
        subset = []
        for i in range(n):
            if selected[i]:
                subset.append(lst[i])
        print(*subset)
        return
    # 재귀 호출
    # 부분집합에 idx 번째 원소 포함
    selected[idx] = 1
    make_subset(idx + 1, selected, n, s + lst[idx])

    # 부분집합에 idx 번째 원소 미포함
    selected[idx] = 0
    make_subset(idx + 1, selected, n, s)


make_subset(0, [0] * N, N, 0)
