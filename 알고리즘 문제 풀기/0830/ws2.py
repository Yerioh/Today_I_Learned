"""
3
3
1 1 2
1
1
5
3 1 2 1 2

#1 2
#2 1
#3 3
"""
T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    N = int(input())  # 저장된 id의 수
    id_list = list(map(int, input().split()))  # N개의 id
    # id를 인덱스로 하는 출입 리스트
    in_out = {}
    for id_data in id_list:
        if in_out.get(id_data):  # 출입 체크를 한번이라도 했다면
            in_out[id_data] += 1
        else:  # 한번도 체크하지 않았다면
            in_out[id_data] = 1
    answer = 0
    for key in in_out:  # 반드시 1명이기에 찾으면 종료
        if in_out[key] % 2:  # 홀수라면 들어와있는 상태
            answer = key
            break
    print(f"#{tc} {answer}")
