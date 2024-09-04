# 완벽한 사각형
def perfect_square(start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    mid_square = mid * mid  # 중앙값으로 만든 사각형
    if mid_square == X:
        return mid
    elif mid_square > X:
        return perfect_square(start, mid - 1)
    else:
        return perfect_square(mid + 1, end)


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T + 1):
    X = int(input())  # 정사각형의 넓이
    answer = perfect_square(0, X)
    print(f"#{tc} {answer}")
