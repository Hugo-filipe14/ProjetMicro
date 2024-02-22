import numpy as np
import matplotlib.pyplot as plt
import os


def Tracer(x, y, xLabel, yLabel, title):
    try:
        for keys in x.keys():
            plt.plot(
                x[keys],
                y[keys],
                label=f"Tension Vgs = {keys}V",
            )
        plt.xlabel(f"{xLabel}")
        plt.ylabel(f"{yLabel}")
        plt.title(f"{title}")
        plt.legend()
        plt.grid()
        # La partie qui suit enregistre les courbes dans un dossier Graphs à la racine du projet
        if not os.path.exists("Graphs"):
            os.makedirs("Graphs")
        plt.savefig(f"./Graphs/{title}.png", format="Png")
        plt.show()
    except Exception as e:
        raise ValueError(f"{e}")


def main():
    # Les clées des dictionnaires sont les tensions Vgs sur lesquelles on travaille
    Vds = {
        "2": [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8],
        "3": [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8],
        "4": [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8],
        "5": [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8],
    }
    I = {
        "2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "3": [
            0,
            0.198,
            0.353,
            0.465,
            0.532,
            0.555,
            0.557,
            0.558,
            0.559,
            0.560,
            0.561,
            0.562,
            0.563,
            0.564,
            0.565,
        ],
        "4": [
            0,
            0.419,
            0.795,
            1.13,
            1.42,
            1.67,
            1.87,
            2.03,
            2.15,
            2.22,
            2.24,
            2.25,
            2.25,
            2.26,
            2.26,
        ],
        "5": [
            0,
            0.639,
            1.24,
            1.79,
            2.31,
            2.78,
            3.21,
            3.59,
            3.93,
            4.23,
            4.49,
            4.70,
            4.87,
            4.99,
            5.0,
        ],
    }
    # Check si les listes de valeurs ont les mêmes dimension
    for keys in Vds.keys():
        print(f"{len(Vds[keys])} points pour Vds={keys}")
    for keys in I.keys():
        print(f"{len(I[keys])} points pour I={keys}")
    # On trace les courbes nécessaires
    Tracer(
        Vds,
        I,
        "Tension Vds en V",
        "Courant I en A",
        "Caractéristique I(Vds) d'un transistor NMOS",
    )
    return 0


if __name__ == "__main__":
    main()
