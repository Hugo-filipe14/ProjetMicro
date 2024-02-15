import numpy as np
import matplotlib.pyplot as plt
import os 
def Tracer(x, y, xLabel, yLabel, title):
    try:
        for keys in x.keys():
            plt.plot(
                x[keys],
                y[keys],
                label=f"Tension Vds = {keys}",
            )
        plt.xlabel(f"{xLabel}")
        plt.ylabel(f"{yLabel}")
        plt.title(f"{title}")
        plt.grid()
        # La partie qui suit enregistre les courbes dans un dossier Graphs à la racine du projet
        if  not os.path.exists("Graphs"):
            os.makedirs("Graphs")
        plt.savefig(f"./Graphs/{title}.png", format="Png")
        plt.show()
    except Exception as e:
        raise ValueError(f"{e}")


def main():
    # Les clées des dictionnaires sont les tensions Vgs sur lesquelles on travaille
    Vds = {
        "5": [
            0,
            0.2,
            0.4,
            0.6,
            0.8,
            1.0,
            1.2,
            1.4,
            1.6,
            1.8,
            2.0,
            2.2,
            2.4,
            2.6,
            2.8,
        ],
        "10": [
            0,
            0.2,
            0.4,
            0.6,
            0.8,
            1.0,
            1.2,
            1.4,
            1.6,
            1.8,
            2.0,
            2.2,
            2.4,
            2.6,
            2.8,
        ],
        "15": [
            0,
            0.2,
            0.4,
            0.6,
            0.8,
            1.0,
            1.2,
            1.4,
            1.6,
            1.8,
            2.0,
            2.2,
            2.4,
            2.6,
            2.8,
        ],
    }
    I = {
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
        "10": [
            0,
            1.74,
            3.44,
            5.0,
            # A partir de ces valeurs Tinckercad sature la tension
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
        ],
        "15": [
            0,
            2.84,
            # A partir de ces valeurs Tinckercad sature la tension
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
            5.0,
        ],
    }
    # Check si les listes de valeurs ont les mêmes dimension
    for keys in Vds.keys():
        print(f"{len(Vds[keys])} points for Vds={keys}")
    for keys in I.keys():
        print(f"{len(I[keys])} points for I={keys}")
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
