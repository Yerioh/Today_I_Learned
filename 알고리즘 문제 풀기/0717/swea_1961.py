import sys
sys.stdin = open("swea_1961.txt", "r")

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    # 행렬의 크기
    N = int(input())
    # 입력받은 NxN행렬
    num_list = [list(input().split()) for _ in range(N)]

    # 회전 함수 정의
    def rotate_list(li):
        new_list = []
        for i in zip(*li[::-1]):
            new_list.append(list(i))
        return new_list
    # 함수 이용 회전한 리스트 선언
    num_list_90 = rotate_list(num_list)
    num_list_180 = rotate_list(num_list_90)
    num_list_270 = rotate_list(num_list_180)
    print(f'#{t}')
    for i in range(N):
        print(f'{"".join(num_list_90[i])} {"".join(num_list_180[i])} {"".join(num_list_270[i])}')
