import sys

sys.stdin = open('txt/input_ws2.txt', 'r')


def bin_search(end_page, search_page):
    start = 1
    end = end_page
    cnt = 0
    while start <= end:
        c = int((start + end) / 2)
        cnt += 1
        if c > search_page:
            end = c
        elif c < search_page:
            start = c
        else:
            return cnt
    # 탐색에 실패하면 제일 큰 값인 끝 페이지를 반환
    return end_page


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    # 전체 페이지 P, A와 B가 각자 찾을 페이지 Pa, Pb
    P, Pa, Pb = map(int, input().split())
    cnt_a = bin_search(P, Pa)
    cnt_b = bin_search(P, Pb)
    answer = 'A' if cnt_a < cnt_b else 'B' if cnt_b < cnt_a else 0
    print(f'#{tc} {answer}')
