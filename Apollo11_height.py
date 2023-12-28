import time
import datetime
from scipy.integrate import odeint
import krpc

connection = krpc.connect(name='Graphics')
vessel = connection.space_center.active_vessel
figure, ax = plt.subplots()
Time = []
Speed = []
Orbit = vessel.orbit.body.reference_framesaved = 999
time.sleep(4)

# Получаем данные
while True:
    Speed.append(vessel.flight(Orbit).mean_altitude)
    Time.append(vessel.met)
    if vessel.met > 85:
        break

# Строим график
ax.plot(Time, Speed)
plt.ylabel('высота, м')
plt.grid(color='black')  
plt.show()
