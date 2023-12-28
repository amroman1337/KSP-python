import matplotlib.pyplot as plt  # библиотека для рисования графиков
import krpc  # библиотека для подключения к KSP и забора данных

connection = krpc.connect(name='Graphics')
vessel = connection.space_center.active_vessel

figure, ax = plt.subplots()
Speed = []
Time = []
Orbit = vessel.orbit.body.reference_frame

# Получаем данные
while True:
    Speed.append((vessel.flight(Orbit).speed * 60) / 1000)
    Time.append(vessel.met / 60)
    if vessel.metvessel.flight(Orbit).speed > 1000:
        break

# Работаем с графиком
ax.plot(Speed, Time)  # рисуем график
plt.xlabel('Время, сек')
plt.ylabel('Скорость, м/с')
plt.grid(color='black')  # наводим красоту
plt.show()
