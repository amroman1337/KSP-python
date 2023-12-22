import matplotlib.pyplot as plt  # подключаем библиотеку для рисования графиков


import math  # подключаем библиотеку для получения констант е, пи и тригонометрических функций


def Toplivo(M0, M, t):
    return (M0 - M) / t


# константы и стартовые значения:

t0 = 165  # время работы ступени в секундах
b0 = 90  # начальный угол в градусах
g0 = 9.81
G = 6.6743 * 10 ** (-11)   # гравитационная постоянная Земли
Mz = 5.9736 * 10 ** 24   # масса Земли
R = 6371 * 10 ** 3    # радиус Земли
M_start = 2889 * 10 ** 3   # масса ракеты до запуска
M_end = M_start - 2071 * 10 ** 3   # масса после полного расхода топлива 1-ой ступени
Ft0 = 34343 * 10 ** 3     # тяга ускорителя 1-ой ступени
v0 = 0
h0 = 0
k = Toplivo(M_start, M_end, t0)   # расход топлива в секунду
ay0 = (Ft0 / M_start) * math.sin(math.radians(b0)) - g0
ax0 = (Ft0 / M_start) * math.cos(math.radians(b0))
v0y = v0 * math.sin(math.radians(b0)) + ay0
v0x = v0 * math.cos(math.radians(b0)) + ax0
V0 = []
H0 = []

for t in range(t0):
    Mt = M_start - k * t    # масса ракеты в данную секунду
    if t == 0:
        v = v0
    else:
        v0y = v0 * math.sin(math.radians(b0)) + ay0
        v0x = v0 * math.cos(math.radians(b0)) + ax0
        v = math.sqrt(v0x ** 2 + v0y ** 2)  # получаем скорость
    if t == 0:
        h = h0
    else:
        h = h0 + v0y + (ay0 / 2)  # получаем высоту

    ay0 = (Ft0 / Mt) * math.sin(math.radians(b0)) - g0
    ax0 = (Ft0 / Mt) * math.cos(math.radians(b0))
    g0 = (G*Mz) / ((R + h)**2)
    V0.append(v)
    H0.append(h)
    b0 = b0 - 70 / t0
    h0 = h
    v0 = v


tm = [i for i in range(t0)]
figure = plt.figure()
ax1 = figure.add_subplot(1, 2, 1)  # создаем график номер 1
ax2 = figure.add_subplot(1, 2, 2)  # создаем график номер 2
ax1.plot(tm, V0)  # график зависимости скорости от времени
ax2.plot(tm, H0)  # график зависимости высоты от времени
plt.show()