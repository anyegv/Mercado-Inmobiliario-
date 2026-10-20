import matplotlib
from matplotlib import pyplot as plt
import Funciones
from Funciones import alq

x_ll=Funciones.servicios_alquileres("servicios")

pr=Funciones.precios_alquileres()
for i in range(len(pr)):
    for j in range(len(pr)-1):
        if pr[j]>pr[j+1]:
            pr[j], pr[j+1]=pr[j+1],pr[j]
            x_ll[j], x_ll[j+1]=x_ll[j+1],x_ll[j]

y_l=[]
for i in range(len(x_ll)):
    for j in range(len(x_ll[i])):
        y_l.append(i)

x_l=[]
for i in range(len(x_ll)):
    for j in range(len(x_ll[i])):
        x_l.append(x_ll[i][j])

plt.figure(
            figsize=(14,8),
            facecolor="#d4d4d4")

plt.scatter(x_l,y_l,
            s=50,
            facecolor="#1757C6",
            #color="#130303"
            )
plt.xticks(
    ticks=range(8),
    fontsize=16,
    fontname="Bell MT",
    labels=["Respaldo\n Energético","Tanque de\n Agua","Teléfono Fijo","Wifi","Climatización","Gas de la\n Calle","Calentador","Lavadora"]
    )
plt.yticks(
    ticks=range(30),
    labels=pr,
    fontname="Bell MT",
    fontsize=15
)
plt.grid(True)
plt.show()