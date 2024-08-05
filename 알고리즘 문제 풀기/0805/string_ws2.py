import sys

sys.stdin = open('txt/input_ws2.txt', 'rt', encoding='UTF8')

T = 10  # 테스트 케이스의 수
for _ in range(T):
    tc = int(input())  # 테스트 케이스 번호
    P = input()  # 찾을 문자열
    text = input()  # 전체 텍스트
    answer = 0  # 정답 초기화
    pl = len(P)  # 패턴의 길이
    tl = len(text)  # 텍스트의 길이
    pi = 0  # 패턴의 인덱스
    ti = 0  # 텍스트의 인덱스
    while pi < pl and ti < tl:
        # P[pi] 와 text[ti] 비교
        if P[pi] != text[ti]:
            ti = ti - pi
            pi = -1

        # 다음 비교 위치로 이동
        ti += 1
        pi += 1

        # pi가 패턴의 길이만큼 되면 패턴 발견
        if pi == pl:
            answer += 1
            # 다음 비교 위해서 다음 시작 위치로 이동
            ti = ti - pi + 1
            pi = 0
    print(f'#{tc} {answer}')