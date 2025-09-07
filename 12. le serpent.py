from jeu import *

x = 100
y = 100
direction = "bas"
pas = 10
couleur = couleur_au_hasard()

while True:

    choisir_couleur(couleur)
    dessiner_point(x, y)

    if touche_haut():
        direction = "haut"
    if touche_bas():
        direction = "bas"
    if touche_droite():
        direction = "droite"
    if touche_gauche():
        direction = "gauche"

    if direction == "haut":
        y = y - 10
    if direction == "bas":
        y = y + 10
    if direction == "gauche":
        x = x - 10
    if direction == "droite":
        x = x + 10

    if not dans_la_fenetre(x, y):
        x = nombre_au_hasard(800)
        y = nombre_au_hasard(800)
        couleur = couleur_au_hasard()

    mettre_ecran_a_jour()
