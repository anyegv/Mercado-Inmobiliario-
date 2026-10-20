import matplotlib
from  matplotlib import pyplot as plt
def barras(x,y):
        plt.figure(
        figsize=(14,6.2),
        facecolor="#d4d4d4")

        plt.bar(x,y,
                width=0.5,
                align="center",
                bottom=0,
                color="#2531D8",
                edgecolor="#9E0303",
                )
        plt.xticks(
                fontname="Algerian",
                fontsize=20,
                color="black",
                fontweight="bold")
        plt.yticks([0,5,10,15,20],
                fontname="Algerian",
                fontsize=15)
        plt.xlim(-0.5,1.5)
        plt.ylim(0,20)
        plt.title("Cantidad de varones y hembras en el curso",
                fontsize=20,
                fontname="Algerian",
                loc="center",
                pad=10,
                color="#000000")
        plt.text(0,18,"18", ha="center", va="bottom",
                fontname="Calibri",
                fontsize=13,
                fontweight="bold")
        plt.text(1,10,"10", ha="center", va="bottom",
                fontname="Calibri",
                fontsize=13,
                fontweight="bold")
        plt.hlines(18,-0.5,-0.25,
                linestyles="--",
                colors="#2531D8",
                linewidth=1)

        plt.hlines(10,-0.5,1.25,
                linestyles="--",
                colors="#2531D8",
                linewidth=1)
        plt.xlabel("Genero",
                fontname="Algerian",
                fontsize=25)
        plt.ylabel("Cantidad",
                fontname="Algerian",
                fontsize=25,
                labelpad=20)
        plt.grid(False)
        return plt.show()
barras(["Hembras","Varones"],[18,10])