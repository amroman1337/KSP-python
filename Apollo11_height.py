 import matplotlib.pyplot as plt  # библиотека для рисования графиков
 import krpc  # библиотека для подключения к KSP и сбора данных
 import time
 import datetime
 from scipy.integrate import odeint

 connection = krpc.connect(name='Graphics')
 vessel = connection.space_center.active_vessel
 figure, ax = plt.subplots()
 Time = []
 Height = []
 Orbit = vessel.orbit.body.reference_framesaved = 999
 time.sleep(4)

 # Получаем данные
 while True:
 	Height.append(vessel.flight(Orbit).mean_altitude)
 	Time.append(vessel.met)
 	if vessel.met > 85:
     	break

 # Строим график
 ax.plot(Time, Speed)
 plt.xlabel('Время, сек')
 plt.ylabel('высота, м')
 plt.grid(color='black') 
 plt.show()
