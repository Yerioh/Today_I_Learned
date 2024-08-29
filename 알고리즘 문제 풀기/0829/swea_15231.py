import sys

sys.stdin = open("txt/in_15231.txt", "r")

T = int(input())  # 테스트 케이스의 수
answer = [' '] * T
for tc in range(1, T + 1):
    N, V = map(int, input().split())  # 노드의 개수 N, 기준 정점 V
    level = len(bin(N)[2:]) - 1  # 마지막 정점의 레벨
    v_level = len(bin(V)[2:]) - 1  # 기준 정점의 레벨
    if v_level > 0 and N < 2 ** level + 2 ** (level - 1) and V < 2 ** v_level + 2 ** (v_level - 1):
        level -= 1
    answer[tc - 1] = f"#{tc} {level + v_level}"
print(*answer, sep='\n')

#  ㅈㄴ 어렵네....
# 내가 이겼다!!!!!
