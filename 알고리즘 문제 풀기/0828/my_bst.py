def binary_search_tree(target, root):
    if bst[root] == 0:
        bst[root] = target
    else:
        if target < bst[root]:
            if bst[lc[root]]:
                binary_search_tree(target, lc[root])
            else:
                bst[lc[root]] = target
        elif target > bst[root]:
            if bst[rc[root]]:
                binary_search_tree(target, rc[root])
            else:
                bst[rc[root]] = target


N = int(input())  # 입력받을 리스트의 길이
arr = list(map(int, input().split()))  # 이진 탐색 트리로 바꿀 리스트
lc = [0] * (2 ** N)  # 왼쪽 자식 노드
rc = [0] * (2 ** N)  # 오른쪽 자식 노드
for i in range(2, 2 ** N):
    if i % 2:
        rc[i // 2] = i
    else:
        lc[i // 2] = i
bst = [0] * (2 ** N)
for num in arr:
    binary_search_tree(num, 1)
print(bst)
