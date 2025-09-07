from jeu import *

while True:
    couleur = couleur_au_hasard()
    choisir_couleur(couleur)

    x = nombre_au_hasard(800)
    y = nombre_au_hasard(800)
    dessiner_point(x, y)

    # x1 = nombre_au_hasard(800)
    # y1 = nombre_au_hasard(800)
    # x2 = nombre_au_hasard(800)
    # y2 = nombre_au_hasard(800)
    # dessiner_ligne(x1, y1, x2, y2)

    mettre_ecran_a_jour()
