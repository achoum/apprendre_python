from jeu import *

while True:

    effacer_ecran()

    if touche_haut():
        jouer_son("boing")

    if touche_bas():
        jouer_son("loup")

    if touche_droite():
        jouer_son("monstre")

    if touche_gauche():
        jouer_son("prout")

    mettre_ecran_a_jour()
