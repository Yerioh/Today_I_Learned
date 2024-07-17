N = int(input()) # 입력받은 정수(10 <= N <= 1000)
list_369 = [] # 369게임을 담을 리스트
for i in range(1, N+1): # N 만큼 반복
    count = 0 # 369의 개수 초기화
    for s in str(i): # 숫자를 문자열로 바꾸어 369 찾기
        if s in ["3","6","9"]:
            count += 1 # 있다면 카운트+1
    if count == 0: # 카운트의 개수가 없다면 숫자
        list_369.append(str(i))
    else: # 카운트의 개수가 있다면 카운트 수만큼 박수
        list_369.append("-"*count)
print(list_369)