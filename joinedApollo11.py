import matplotlib.pyplot as plt

import numpy as np

# параметры ракеты и взлёта

TIME = 165  # время работы первой ступени
M0 = 2889 * 10 ** 3  # начальная масса корабля
FT = 34343 * 10 ** 3  # тяга ускорителя 1-ой ступени
K = 12551.5  # скорость расхода топлива
B = -0.0072  # изменение угла движения ракеты рад/с
C_F = 0.8  # коэф сопротивления
S = 2954 ** (2 / 3)  # площадь лобового сопротивления

# параметры ракеты и взлёта для KSP

TIME2 = 85  # время работы первой ступени
M02 = 431 * 10 ** 3  # начальная масса корабля
FT2 = 6781.2 * 10 ** 3  # тяга ускорителя 1-ой ступени
K2 = 2470.6  # скорость расхода топлива
B2 = -0.001  # изменение угла движения ракеты рад/с
C_F = 0.2  # коэф сопротивления
S = 1534 ** (2 / 3)  # площадь лобового сопротивления

# константы
e = 2.72
DT = 0.1  # шаг (по желанию изменяемая переменная)
ANG_0 = np.pi / 2
ANG_1 = ANG_0 + TIME2 * B2
G = 9.81
M_A = 0.29
R = 8.31
T = 300
P_0 = 10 ** 5
GAZ_P = M_A / (R * T)

x_values = [0]
y_values = [0]
vx_values = [0]
vy_values = [0]
ax_values = [0]
ay_values = [-9.81]

x = 0
y = 0
vx = 0
vy = 0
ax = 0
ay = 0

for i in range(int(TIME // DT)):  # рассчитываем n секунд шагов первой ступени
    t = i * DT
    rho = (GAZ_P * P_0) * (e ** (-G * y * GAZ_P))
    f_cx = C_F * S * (rho * (vx_values[-1] ** 2) * 0.5)
    f_cy = C_F * S * (rho * (vy_values[-1] ** 2) * 0.5)
    ax = ((FT) * np.cos(ANG_0 + B * t) - f_cx)/(M0 - K * t)
    ay = ((FT) * np.sin(ANG_0 + B * t) - f_cy)/(M0 - K * t) - G
    vx = vx_values[-1] + ax * DT
    vy = vy_values[-1] + ay * DT
    x = x_values[-1] + vx * DT
    y = y_values[-1] + vy * DT
    ax_values.append(ax)
    ay_values.append(ay)
    vx_values.append(vx)
    vy_values.append(vy)
    x_values.append(x)
    y_values.append(y)


x_values2 = [0]
y_values2 = [0]
vx_values2 = [0]
vy_values2 = [0]
ax_values2 = [0]
ay_values2 = [-9.81]

x2 = 0
y2 = 0
vx2 = 0
vy2 = 0
ax2 = 0
ay2 = 0


for i in range(int(TIME2 // DT)):  # рассчитываем n секунд шагов первой ступени
    t = i * DT
    rho = (GAZ_P * P_0) * (e ** (-G * y2 * GAZ_P))
    f_cx2 = C_F * S * (rho * (vx_values2[-1] ** 2) * 0.5)
    f_cy2 = C_F * S * (rho * (vy_values2[-1] ** 2) * 0.5)
    ax2 = ((FT2) * np.cos(ANG_0 + B2 * t) - f_cx2)/(M02 - K2 * t)
    ay2 = ((FT2) * np.sin(ANG_0 + B2 * t) - f_cy2)/(M02 - K2 * t) - G
    vx2 = vx_values2[-1] + ax2 * DT
    vy2 = vy_values2[-1] + ay2 * DT
    x2 = x_values2[-1] + vx2 * DT
    y2 = y_values2[-1] + vy2 * DT
    ax_values2.append(ax2)
    ay_values2.append(ay2)
    vx_values2.append(vx2)
    vy_values2.append(vy2)
    x_values2.append(x2)
    y_values2.append(y2)


velocity = [((vx_values[i]) ** 2 + vy_values[i] ** 2) ** 0.5 for i in range(len(vx_values))]
velocity2 = [((vx_values2[i]) ** 2 + vy_values2[i] ** 2) ** 0.5 for i in range(len(vx_values2))]
# print([((vx_values[::10][i]) ** 2 + vy_values[::10][i] ** 2) ** 0.5 for i in range(TIME2)])
# print(y_values[::100])
# plt.plot(range(0, TIME2), vx_values[::int(DT ** -1)])

# plt.xlabel("Время, с")
# plt.ylabel("Высота, м")
# plt.plot(range(0, TIME), y_values[::int(DT ** -1)])
# plt.plot(range(0, TIME2), y_values2[::int(DT ** -1)])
plt.xlabel("Время, с")
plt.ylabel("Скорость, м/с")
plt.plot(range(0, TIME), velocity[::int(DT ** -1)])
plt.plot(range(0, TIME2), velocity2[::int(DT ** -1)])
plt.show()
