from jeu import *


while True:

    effacer_ecran()

    choisir_couleur("bleu")

    t = trouver_taille_de_la_fenetre()
    dessiner_ligne(0, 0, souris_x(), souris_y())
    dessiner_ligne(t, 0, souris_x(), souris_y())
    dessiner_ligne(0, t, souris_x(), souris_y())
    dessiner_ligne(t, t, souris_x(), souris_y())

    choisir_couleur("rouge")
    dessiner_cercle(souris_x(), souris_y(), 200)

    choisir_couleur("vert")
    d = mesure_distance(souris_x(), souris_y(), 0, 0)
    dessiner_cercle(souris_x(), souris_y(), d)

    mettre_ecran_a_jour()
