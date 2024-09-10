N = 10
# N개의 원소가 있고, 집합을 만드려고 한다.
p = [i for i in range(N)]
# p[i] => i가 가리키고 있는 사람 번호 => 대표 O or X

# 연산의 최적화를 위해서 트리의 높이를 관리하는 rank 배열
rank = [1] * N


# x가 속한 집합의 대푤르 찾는 연산
def find(x):
    # 집합의 대표가 되는 조건?
    # 부모를 가리키는 화살표가 자기 자신을 향할 때 그 친구가 대표
    if p[x] != x:
        # x가 자기자신을 가리키지 않으면 대표를 계속 찾아
        # 경로 압축(바로 대표를 가리키도록)
        p[x] = find(p[x])
    return p[x]


# x가 속한 집합과 y가 속한 집합을 합치는 연산
# 집합을 합친다 => 두 집합의 대표가 같게 한다.
def union(x, y):
    # x가 속한 집합의 대표
    root_x = find(x)
    # y가 속한 집합의 대표
    root_y = find(y)

    # 두 집합의 대표자가 다를때만 합치자
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            p[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            p[root_x] = root_y
        else:
            # 두 집합의 높이가 같을 때는 하나를 다른 한쪽에 붙이고
            # 붙인 쪽 높이 + 1

            # y를 x에 붙인다면
            p[root_y] = root_x
            # x의 높이 증가
            rank[root_x] += 1
