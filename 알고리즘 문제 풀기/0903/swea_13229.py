day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
T = int(input())
for tc in range(1, T + 1):
    S = input()
    print(f"#{tc} {7 - day.index(S)}")
