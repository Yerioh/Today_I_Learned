'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        # 루트 부터 삭제할지 말지 판단
        # 만약 삭제가 되었다면 다른 노드로 대체 되었을 것이다.
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:  # 노드가 없으면 삭제 X
            return node
        if key < node.key:  # key 가 현재 노드보다 작다면
            return self._delete(node.left, key)
        elif key > node.key:  # key 가 현재 노드보다 크다면
            return self._delete(node.right, key)
        else:  # 현재 노드가 삭제 대상 이면
            if node.left is None and node.right is None:  # 단말 노드라면
                node = None
            # 자식이 하나만 있는 경우
            elif node.left is None:  # 오른쪽에만 자식이 있을 경우
                node = node.right
            elif node.right is None:  # 왼쪽에만 자식이 있을 경우
                node = node.left
            else:  # 자식이 둘 다 있는 경우
                min_node_from_right = self._get_min(node.right)
                node.key = min_node_from_right.key

                # 찾은 최소 노드를 여기 위치로 가져오는 것은 그 최소 노드가 원래 있던 자리도 누군가 대체(삭제)
                node.right = self._delete(node.right, min_node_from_right.key)

            # 마지막 삭제 후의 node 자리는 누군가로 대체
            return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left  # 계속 왼쪽 자식으로 이동
        # 마지막 왼쪽 자식이 최소값
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
