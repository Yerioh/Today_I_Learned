import sys

sys.stdin = open('txt/in06.txt', 'r')

T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    arr = list(map(int, input()))  # 문자열을 정수형 리스트로
    answer = 0  # 고용해야할 사람의 수
    cnt = 0  # 현재 기립 박수 중인 사람의 수
    for i in range(len(arr)):
        # 조건에 해당하는 인원이 있고, 현재 기립 박수 치는 사람이 조건 미만이라면,
        if arr[i] != 0 and cnt < i:
            answer += (i - cnt)
            cnt += (i - cnt)
        if i <= cnt:
            cnt += arr[i]
    print(f'#{tc} {answer}')
