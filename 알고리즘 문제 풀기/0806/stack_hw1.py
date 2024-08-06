# T = int(input())  # 테스트 케이스의 수
# for tc in range(1, T + 1):
#     N = int(input())  # 입력 받은 정수 N
#     answer = []
#     for i in range(N):  # N만큼 반복
#         li = []  # 숫자를 담을 임시 리스트
#         for j in range(i + 1):
#             if j == 0 or j == i:  # 처음과 마지막은 1
#                 li.append(1)
#             else:  # 처음과 마지막이 아니면 인덱스 활용하여 값 참조
#                 li.append(answer[i - 1][j - 1] + answer[i - 1][j])
#         answer.append(li)
#     print(f"#{tc}")
#     for i in range(N):
#         print(*answer[i])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 삼각형의 크기 N
    answer = [[]] * N  # 정답을 담을 2차원 배열
    for i in range(N):
        if i == 0:  # 첫 값은 [1]
            temp = [1]
        else:
            temp = [0] * (i + 1)  # 숫자들을 담을 배열
            lst = answer[i - 1] + [0]  # 비교하기 위한 배열
            stack = 0  # 현재 위치보다 앞
            for j in range(i + 1):
                temp[j] = stack + lst[j]
                stack = lst[j]
        answer[i] = temp
    print(f'#{tc}')
    for a in answer:
        print(*a)
