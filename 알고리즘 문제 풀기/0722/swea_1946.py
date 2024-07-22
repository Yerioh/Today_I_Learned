import sys
sys.stdin = open('input_1946.txt','r')

# 테스트 케이스의 수
T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 압축 리스트
    zip_list = [list(input().split()) for _ in range(N)]

    # 압축을 푼 리스트
    new_list = []
    for i in zip_list:
        for j in range(int(i[1])):
            new_list.append(i[0])

    # 답변 초기화
    answer = []

    # 10개씩 묶기
    for i in range(len(new_list)//10 + 1):
        temp_list = []
        if i == len(new_list)//10:
            for j in range(len(new_list)%10):
                temp_list.append(new_list[i*10 + j])
        else:
            for j in range(10):
                temp_list.append(new_list[i*10 + j])
        answer.append(temp_list)
        
    print(f'#{t}')
    for i in answer:
        print(''.join(i))