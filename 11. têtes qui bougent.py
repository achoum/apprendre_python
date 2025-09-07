from jeu import *

from dataclasses import dataclass

# Définir ce qu'il y a dans une tête.


@dataclass
class Tete:
    nom: QuelqueChose
    x: QuelqueChose = 0
    y: QuelqueChose = 0
    vitesse_x: QuelqueChose = 0
    vitesse_y: QuelqueChose = 0


# Créer les têtes.
famille = [
    Tete(nom="anja"),
    Tete(nom="mamie"),
    Tete(nom="papi"),
    Tete(nom="amandine"),
    Tete(nom="mathieu"),
]

# Choisir au hasard la position et la vitesse de chaque tête.
taille_de_la_fenetre = trouver_taille_de_la_fenetre()
for tete in famille:
    tete.x = nombre_au_hasard(taille_de_la_fenetre)
    tete.y = nombre_au_hasard(taille_de_la_fenetre)
    tete.vitesse_x = nombre_au_hasard(6)
    tete.vitesse_y = nombre_au_hasard(6)


while True:

    effacer_ecran()

    # Pour toutes les têtes une après l'autre.
    for tete in famille:

        # Faire bouger la tete.
        tete.x = tete.x + tete.vitesse_x
        tete.y = tete.y + tete.vitesse_y

        # Si la tête sort de l'écran, inverser la vitesse pour
        # la faire revenir.
        if tete.x > taille_de_la_fenetre or tete.x < 0:
            tete.vitesse_x = -tete.vitesse_x

        if tete.y > taille_de_la_fenetre or tete.y < 0:
            tete.vitesse_y = -tete.vitesse_y

        # Dessiner la tête.
        dessiner_image(tete.x, tete.y, tete.nom)

    mettre_ecran_a_jour()
