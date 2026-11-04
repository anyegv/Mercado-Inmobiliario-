import matplotlib
from matplotlib import pyplot as plt

y=[15000,23000,30000,36000,38500,60000]
x=["Apartamento","Casas","Colonial","Biplanta","Casa de campo","Casas \nIndependientes"]
plt.figure(figsize=(12,6),
        facecolor="#dccfcf"
        )
plt.barh(x,y,
        height=0.7,
        color="#1D6ACE",
        edgecolor="black")
#plt.subplots_adjust(left=0.15, right=0.9, top=0.95, bottom=0.03)
plt.yticks(ticks=range(6),
        fontsize=14,
        fontname="Bell MT"
        )
plt.xticks(fontsize=14,
        fontname="Bell MT")
plt.ylabel("Tipos de vivienda",
        fontname="Bell MT",
        fontsize=20,
        loc="center",
        labelpad=1)
plt.xlabel("Mediana del Precio",
        fontname="Bell MT",
        fontsize=20,
        loc="center",
        labelpad=10)
for i in range(len(y)):
        plt.text((y[i]//2.25),i-0.1, f"${y[i]}",
                color="#ffffff",
                fontname="Bell MT",
                fontsize=20)
#plt.grid(linestyle="--", alpha=0.4)
plt.ylim(-1,6)
plt.vlines(y, ymin=-1, ymax=range(len(y)), linestyles="--", linewidth=1, colors="blue" )
plt.title("Precio Mediano por Tipo de Vivienda",
        fontname="Bell MT",
        fontsize=24)
plt.show()