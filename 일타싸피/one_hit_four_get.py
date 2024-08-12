# 해당 코드는 SSAFY에서 진행된 일타싸피 과목평가, 반 대항전에서 사용된 코드입니다.
# 스켈레톤 코드에서 각도와 파워를 구하기 위한 코드만 적혀있습니다.
# 해당 코드만으로는 프로그램을 진행할 수 없습니다.

import math

angle = 0.0
power = 0.0

order = 0
balls = [[0, 0] for _ in range(6)]
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

whiteBall_x = balls[0][0]
whiteBall_y = balls[0][1]

# targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
targetBall_x = 0
targetBall_y = 0
print('내 턴:', order)
# 공의 목록에서 목적구를 찾기 위해 반복
for i in range(1, 6):
    if i == 5 and balls[i][0] > 0 and balls[i][1] > 0:
        targetBall_x = balls[i][0]
        targetBall_y = balls[i][1]
    if order == 1:  # 선공일 경우
        if i % 2 == 1 and balls[i][0] > 0 and balls[i][1] > 0:
            targetBall_x = balls[i][0]
            targetBall_y = balls[i][1]
            break
    elif order == 2:  # 후공일 경우
        if i % 2 == 0 and balls[i][0] > 0 and balls[i][1] > 0:
            targetBall_x = balls[i][0]
            targetBall_y = balls[i][1]
            break
print('현재 목적구:', targetBall_x, targetBall_y)

# 목적구에서 가까운 홀 찾기
hole_x, hole_y = 0, 0
min_distance = 500
for temp_x, temp_y in HOLES:
    t_h_x = abs(targetBall_x - temp_x)
    t_h_y = abs(targetBall_y - temp_y)
    t_h_dist = math.sqrt(t_h_x ** 2 + t_h_y ** 2)
    if t_h_dist < min_distance:
        min_distance = t_h_dist
        hole_x, hole_y = temp_x, temp_y

# # 홀 위치 조정
# n = 1.5
# if hole_x == 0:
#     hole_x += n
# elif hole_x == 254:
#     hole_x -= n
# if hole_y == 0:
#     hole_y += n
# elif hole_y == 127:
#     hole_y -= n
print('공을 넣을 홀:', hole_x, hole_y)

# 내 공을 보낼 위치 point 구하기
radian1 = math.atan(abs(targetBall_x - hole_x) / abs(targetBall_y - hole_y))
point_x, point_y = 0, 0
r = 5.73  # 공의 직경
point_distance = min_distance + r
# x 좌표
if targetBall_x < hole_x:
    point_x = hole_x - (point_distance * math.sin(radian1))
elif targetBall_x > hole_x:
    point_x = hole_x + (point_distance * math.sin(radian1))
else:
    point_x = hole_x
# y 좌표
if targetBall_y < hole_y:
    point_y = hole_y - (point_distance * math.cos(radian1))
elif targetBall_y > hole_y:
    point_y = hole_y + (point_distance * math.cos(radian1))
else:
    point_y = hole_y
print('공을 보낼 위치: ', point_x, point_y)

# width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
width = abs(point_x - whiteBall_x)
height = abs(point_y - whiteBall_y)

# radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
#   - 1radian = 180 / PI (도)
#   - 1도 = PI / 180 (radian)
# angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
radian = math.atan(width / height) if height > 0 else 0
angle = 180 / math.pi * radian

# point가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
if whiteBall_x == point_x:
    if whiteBall_y < point_y:
        angle = 0
    else:
        angle = 180
elif whiteBall_y == point_y:
    if whiteBall_x < point_x:
        angle = 90
    else:
        angle = 270

# point가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
if whiteBall_x > point_x and whiteBall_y > point_y:
    radian = math.atan(width / height)
    angle = (180 / math.pi * radian) + 180

# point가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
elif whiteBall_x < point_x and whiteBall_y > point_y:
    radian = math.atan(height / width)
    angle = (180 / math.pi * radian) + 90

# point가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
elif whiteBall_x > point_x and whiteBall_y < point_y:
    radian = math.atan(height / width)
    angle = (180 / math.pi * radian) + 270

# distance: 두 점(좌표) 사이의 거리를 계산
distance = math.sqrt(width ** 2 + height ** 2) + min_distance

# power: 거리 distance에 따른 힘의 세기를 계산
power = distance * 0.275
power = 100 if power > 100 else power