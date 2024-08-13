# 해당 코드는 SSAFY 12기 일타싸피 전국대항전용 코드입니다.
# 해당 코드는 팀에서 작성한 알고리즘만 작성 되어있습니다.
# 해당 코드만으로는 프로그램을 실행할 수 없습니다.

import math

angle = 0.0
power = 0.0
dia = 5.73

order = 0   # 선1 후공2
balls = [[0, 0] for _ in range(6)]  # 프로그램 실행시 들어오는 공들의 위치
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]  # 홀의 기본 위치


# 목적구를 치는 알고리즘의 기본 원리
# 1. 목적구는 balls 의 1 3 5 에 순차적으로 저장, 그 중 값이 있는 것(x, y > 0)만 적용
# 2. 목적구를 넣기에 최적의 홀(hole_x, hole_y)을 선택, 목적구와 해당 홀을 이용하여 공을 보낼 접점(point)의 위치 계산
# 3. 내 공과 point의 거리, 목적구와 홀의 거리를 다 적용하여 power 산출
# 4. 파울? 그런거 모르겠고 3파울 되기 전에 이기면 됩니다.

def get_distance(ball1, ball2, ball3):
    global dia
    drz = math.sqrt((ball1[0] - ball2[0]) ** 2 + (ball1[1] - ball2[1]) ** 2)
    # ball1 과 ball 2 사이의 거리가 drz이고
    dr = math.sqrt(dia ** 2 + drz ** 2)
    # ball 1과 ball 2 사이의 걸이와 직격의 빗변길이 dr

    dr1 = math.sqrt((ball1[0] - ball3[0]) ** 2 + (ball1[1] - ball3[1]) ** 2)
    # ball1과 ball3 사이의 거리 dr3
    dr2 = math.sqrt((ball2[0] - ball3[0]) ** 2 + (ball2[1] - ball3[1]) ** 2)
    # ball2와 ball3 사이의 거리 dr2
    theta = math.atan2(ball1[1] - ball2[1], ball1[0] - ball2[0])
    # ball1과 ball2 사이의 기울기 구하기
    distance = abs(math.tan(theta) * (ball3[0] - ball1[0]) + ball1[1] - ball3[1]) / math.sqrt(
        math.tan(theta) ** 2 + 1)
    # ball1과 ball2를 지나느 직선을 만든다. x축 기준으로 y=ax+b를 알고 그 직선과 ball3 사이의 거리 구하는 공식

    if distance < dia and (dr > dr2 or dr > dr1):
        return False
    # 거리가 직경을 벗어나거나, 그 사이에 있을 때, 가능한 최대 거리를 벗어난 경우 False를
    return True
    # 아닌 경우 True를 반환해준다.


# whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
whiteBall_x = balls[0][0]
whiteBall_y = balls[0][1]

# targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
targetBall_x = 0
targetBall_y = 0
print(order)
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

nx, ny = dia / 2, dia / 2

# 수정을 위한 hole 가져오기

# 세로 벽에 구석에 붙어있다?(hole 기준 지름 만큼 dy가 있으면) ny를 추가 또는 빼주기
if targetBall_x < dia or 254 - dia < targetBall_x < 254:
    ny = 0
# 가로 벽에 구석에 붙어있다?(hole 기준 지름 만큼 dx가 있으면) nx를 추가 또는 빼주기
if targetBall_y < dia or 127 - dia < targetBall_y < 127:
    nx = 0
pockets = [[0 + nx, 0 + ny], [127, 0 + ny], [254 - nx, 0 + ny], [0 + nx, 127 - ny], [127, 127 - ny],
            [254 - nx, 127 - ny]]
# target공 위치에 따른 hole 위치 수정본

# 목적구에서 가까운 홀 찾기
hole_x, hole_y = 0, 0
min_minus_angle = 360

for temp_x, temp_y in pockets:
    t_h_x = targetBall_x - temp_x
    t_h_y = targetBall_y - temp_y
    t_h_angle = math.atan2(t_h_x, t_h_y)
    if t_h_angle < 0:
        t_h_angle += math.pi * 2

    w_t_x = whiteBall_x - targetBall_x
    w_t_y = whiteBall_y - targetBall_y
    w_t_angle = math.atan2(w_t_x, w_t_y)
    if w_t_angle < 0:
        w_t_angle += math.pi * 2

    if abs(t_h_angle - w_t_angle) < min_minus_angle:
        min_minus_angle = abs(t_h_angle - w_t_angle)
        hole_x, hole_y = temp_x, temp_y

print('공을 넣을 홀:', hole_x, hole_y)

t_h_distance = math.sqrt(abs(targetBall_x - hole_x) ** 2 + abs(targetBall_y - hole_y) ** 2)

# 내 공을 보낼 위치 point 구하기
radian1 = math.atan(abs(targetBall_x - hole_x) / abs(targetBall_y - hole_y))
point_x, point_y = 0, 0

point_distance = t_h_distance + dia

dxh, dyh = targetBall_x - hole_x, targetBall_y - hole_y
ang_h2 = math.atan2(dyh, dxh)
# x축을 기준으로 기울기 구하기

if ang_h2 < 0:
    ang_h2 += math.pi * 2
# -pi부터 pi까지라 0~2pi까지 맞춰주기 위해서

point_x = targetBall_x + dia * math.cos(ang_h2)
point_y = targetBall_y + dia * math.sin(ang_h2)
# 해당 각도를 그대로 사용해도 된다.

if not get_distance([whiteBall_x, whiteBall_y], [targetBall_x, targetBall_y], [point_x, point_y]):
    # 범위를 벗어나는지 확인
    dia -= 0.1
    dxh, dyh = targetBall_x - hole_x, targetBall_y - hole_y
    ang_h2 = math.atan2(dyh, dxh)

    if ang_h2 < 0:
        ang_h2 += math.pi * 2

    point_x = targetBall_x + dia * math.cos(ang_h2)
    point_y = targetBall_y + dia * math.sin(ang_h2)
# 직경을 줄이고 point_x와 point_y를 다시 구한다.
print('공을 보낼 위치: ', point_x, point_y)

# width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
width = abs(point_x - whiteBall_x)
height = abs(point_y - whiteBall_y)

# radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
#   - 1radian = 180 / PI (도)
#   - 1도 = PI / 180 (radian)
# angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
radian = math.atan(width / height) if height > 0 else 0


def hitting_ball(ball1, ball2):

    dx12, dy12 = ball2[0] - ball1[0], ball2[1] - ball1[1]

    ang_12 = math.atan2(dx12, dy12)
    if ang_12 < 0:
        ang_12 += math.pi * 2
    return math.degrees(ang_12)


angle = hitting_ball([whiteBall_x, whiteBall_y], [point_x, point_y])

# distance: 두 점(좌표) 사이의 거리를 계산
distance = math.sqrt(width ** 2 + height ** 2) + t_h_distance

# power: 거리 distance에 따른 힘의 세기를 계산
power = distance * 0.22
power = 70 if power > 70 else power
power = 35 if power < 35 else power