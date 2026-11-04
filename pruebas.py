import matplotlib
from matplotlib import pyplot as plt

def comp_países():
        data=[
                ("Brasil", 7710, 91698),
                ("El Salvador", 5249, 90000),
                ("México", 4792, 96982),
                ("Cuba", 204, 16500)]
        labels=['0']
        years=[0]
        for país, salario, vivienda in data:
                labels.append(f"{país}\nSalario: \\${salario}/año|Casa: \\${vivienda}")
                years.append(vivienda/salario)
        plt.figure(figsize=(14,6),
                facecolor="#eadddd",
                edgecolor="#d45050")
        plt.plot(labels,years,
                marker=".",
                color="blue"
                )
        plt.xticks(fontname="Bell MT",
                fontsize=12
                )
        plt.yticks(fontname="Bell MT",
                fontsize=15
                )
        plt.xlim(0,4.5)
        plt.ylim(0,90)
        plt.xlabel("Países con sus Salarios Promedios y Precio Promedio de Casas en Venta",
                fontname="Bell MT",
                fontsize=18,
                labelpad=8)
        plt.ylabel("Años de salario íntegro necesarios\n para comprar la vivienda",
                fontname="Bell MT",
                fontsize=18,
                labelpad=10)
        plt.grid(linestyle="--", alpha=0.4)
        plt.title("Años para comprar una vivienda destinando el 100% del salario anual (2025)",
                fontname="Bell MT",
                fontsize=20,
                color="black")
        plt.vlines(x=labels, ymin=-10, ymax=years, linestyles="--", linewidth=1, colors="blue")
        return plt.show()
comp_países()