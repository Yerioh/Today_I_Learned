def baby_gin(number):
    counts = [0] * 12  # run 검사 시 IndexError 발생 방지
    #  0~9 까지의 숫자의 개수를 count
    for n in str(number):
        counts[int(n)] += 1
    # triplet 과 run 을 확인하기 위한 변수
    triplet = run = 0
    # triplet 과 run 을 검출하지 못할 경우를 생각해 while 문 사용하여 반복
    i = 0
    while i < 10:
        # triplet 검출 시 해당 인덱스를 다시 검사하도록 continue 문 사용
        if counts[i] >= 3:
            counts[i] -= 3
            triplet += 1
            continue
        # run 검출 시 해당 인덱스를 다시 검사하도록 continue 문 사용
        if counts[i] >= 1 and counts[i + 1] >= 1 and counts[i + 2]:
            counts[i] -= 1
            counts[i - 1] -= 1
            counts[i - 2] -= 1
            run += 1
            continue
        # 검출하지 못한 경우에만 i 증가
        i += 1
    return 'baby-gin' if triplet + run == 2 else 'lose'


num_list = [644544, 123123, 235777]
for num in num_list:
    print(baby_gin(num))
