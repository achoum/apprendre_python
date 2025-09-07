"""Petite librairie pour apprendre à programmer des jeux vidéo en français.

Par Mathieu Guillame-Bert.
"""

from typing import Literal, Optional, Tuple, Dict, Any

import dataclasses
import sys
import random
import os
import pygame
import time
import math

# Les nom de couleurs
Couleur = Literal["bleu", "rouge", "vert", "blanc", "noir"]

QuelqueChose = Any

# Comment convertir les noms de couleur en couleur additive Rouge, Vert et Bleu.
# Le nombre varie entre 0 (pas de couleur additive) et 255 (maximum de couleur additive).
_DICTIONAIRE_COULEURS: Dict[Couleur, Tuple[int, int, int]] = {
    "bleu": (0, 0, 255),
    "rouge": (255, 0, 0),
    "vert": (0, 255, 0),
    "noir": (0, 0, 0),
    "blanc": (255, 255, 255),
}

# Le nom des dossiers contenant les images et sons.
_IMAGE_DIR = "image"
_SOUND_DIR = "son"


@dataclasses.dataclass
class _DonneeJeu:
    """
    Le gestionnaire de jeu.

    Attributs:
        fermer_jeu: Indique si le jeu doit être fermé.
        screen: La surface d'affichage principale du jeu.
        clock: L'horloge pour contrôler la fréquence d'images.
        couleur: La couleur principale utilisée dans le jeu (format RGB).
        images: Dictionnaire des images chargées, indexées par nom.
        sons: Dictionnaire des sons chargés, indexés par nom.
    """

    fermer_jeu: bool = False
    screen: Optional[pygame.Surface] = None
    clock: Optional[pygame.time.Clock] = None
    couleur: Tuple[int, int, int] = (255, 0, 0)
    images: Dict[str, pygame.Surface] = dataclasses.field(default_factory=dict)
    sons: Dict[str, pygame.mixer.Sound] = dataclasses.field(default_factory=dict)


# Le gestionnaire de jeu globale.
donnee_jeu = _DonneeJeu()


def affiche_les_functions():
    """Affiche les functions disponible."""

    filtered = {
        "os",
        "pygame",
        "random",
        "typing",
        "dataclasses",
        "sys",
        "random",
        "time",
        "math",
    }
    print("Les functions de jeu sont:")
    print("==========================")

    for x in dir(sys.modules[__name__]):
        if x.startswith("_") or x[0].isupper() or x in filtered:
            continue
        print(x)

    print("==========================")


def attendre(seconds) -> None:
    """Attendre un certain nombre de secondes."""
    time.sleep(seconds)


def couleur_au_hasard() -> Couleur:
    """Choisit une couleur au hasard."""
    # Does not include black and write
    return random.choice(["bleu", "rouge", "vert"])


def trouver_taille_de_la_fenetre() -> int:
    """Donne la largeur de la fenêtre en pixels."""
    return 800


def dans_la_fenetre(x: int, y: int) -> bool:
    """Teste si un point est dans la fenêtre."""
    return (
        x >= 0
        and y >= 0
        and x < trouver_taille_de_la_fenetre()
        and y < trouver_taille_de_la_fenetre()
    )


def souris_x() -> int:
    """Donne la position horizontale de la souris."""
    return pygame.mouse.get_pos()[0]


def souris_y() -> int:
    """Donne la position verticale de la souris."""
    return pygame.mouse.get_pos()[1]


def souris_bouton() -> int:
    """Teste si le bouton de la souris est pressé."""
    return pygame.mouse.get_pressed()[0]


def jouer_son(nom_de_fichier: str) -> None:
    """Joue un son."""
    assert donnee_jeu.screen is not None
    if nom_de_fichier not in donnee_jeu.images:
        path = _filename_to_path(_SOUND_DIR, nom_de_fichier, "wav")
        son = pygame.mixer.Sound(path)
        donnee_jeu.sons[nom_de_fichier] = son
    else:
        son = donnee_jeu.sons[nom_de_fichier]

    son.play()


def dessiner_image(x: int, y: int, nom_de_fichier: str) -> None:
    """Dessine une image à une position dans la fenêtre."""
    assert donnee_jeu.screen is not None
    if nom_de_fichier not in donnee_jeu.images:
        path = _filename_to_path(_IMAGE_DIR, nom_de_fichier, "png")
        image = pygame.image.load(path).convert_alpha()
        donnee_jeu.images[nom_de_fichier] = image
    else:
        image = donnee_jeu.images[nom_de_fichier]

    donnee_jeu.screen.blit(
        donnee_jeu.images[nom_de_fichier],
        (x - image.get_width() // 2, y - image.get_height() // 2),
    )


def effacer_ecran() -> None:
    """Efface le contenu de l'écran."""
    assert donnee_jeu.screen is not None
    donnee_jeu.screen.fill((255, 255, 255))


def choisir_couleur(couleur: Couleur) -> None:
    """Sélectionne la couleur utilisée pour dessiner."""
    if couleur not in _DICTIONAIRE_COULEURS:
        _fatal(
            f'La couleur "{couleur}" n\'exist pas. '
            f"Les couleurs possible sont: {list(_DICTIONAIRE_COULEURS.keys())}."
        )
    donnee_jeu.couleur = _DICTIONAIRE_COULEURS[couleur]


def dessiner_ligne(x1: int, y1: int, x2: int, y2: int) -> None:
    """Dessine une ligne."""
    assert donnee_jeu.screen is not None
    pygame.draw.line(donnee_jeu.screen, donnee_jeu.couleur, (x1, y1), (x2, y2), 2)


def dessiner_cercle(x: int, y: int, r: int) -> None:
    """Dessine un cercle."""
    assert donnee_jeu.screen is not None
    pygame.draw.circle(donnee_jeu.screen, donnee_jeu.couleur, (x, y), r, 2)


def dessiner_point(x: int, y: int) -> None:
    """Dessine un point."""
    assert donnee_jeu.screen is not None
    pygame.draw.circle(donnee_jeu.screen, donnee_jeu.couleur, (x, y), 10, 10)


def attendre_pour_toujours():
    """Attend pour toujours et ne fait plus rien."""
    pygame.display.set_caption("Attendre pour toujours")
    while True:
        _loop()


def mesure_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    """Calcule la distance entre deux points."""
    return int(round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)))


def touche_haut() -> bool:
    """Teste si le bouton flèche-vers-le-haut du clavier est pressé."""
    return pygame.key.get_pressed()[pygame.K_UP]


def touche_bas() -> bool:
    """Teste si le bouton flèche-vers-le-bas du clavier est pressé."""
    return pygame.key.get_pressed()[pygame.K_DOWN]


def touche_droite() -> bool:
    """Teste si le bouton flèche-vers-la-droite du clavier est pressé."""
    return pygame.key.get_pressed()[pygame.K_RIGHT]


def touche_gauche() -> bool:
    """Teste si le bouton flèche-vers-la-gauche du clavier est pressé."""
    return pygame.key.get_pressed()[pygame.K_LEFT]


def touche_espace() -> bool:
    """Teste si le bouton espace du clavier est pressé."""
    return pygame.key.get_pressed()[pygame.K_SPACE]


def nombre_au_hasard(jusqua: int) -> int:
    """Calcule un nombre au hasard entre 0 et l'argument."""
    return random.randint(0, jusqua)


def mettre_ecran_a_jour():
    """Met à jour l'écran après avoir dessiné dessus."""
    _loop()


def _fatal(message: str) -> None:
    print(f"""Ho non! Il y a un problème.\n==============\n{message}\n""")
    sys.exit(1)


def _list_files_with_extension(extension):
    file_list = []
    for file in os.listdir("."):
        if file.endswith(f".{extension}"):
            file_list.append(file)
    return file_list


def _filename_to_path(dir: str, filename: str, extension: str) -> str:
    full_filename = os.path.join(dir, f"{filename}.{extension}")
    if not os.path.exists(full_filename):
        available_files = _list_files_with_extension(extension)
        _fatal(
            f'Impossible de trouver le fichier "{full_filename}". '
            f"Les autre fichiers avec la meme extension sont: {available_files}"
        )
    return full_filename


def _ouvrir_fenetre():
    print("Ouvrir la fenetre")
    pygame.init()
    w = trouver_taille_de_la_fenetre()
    donnee_jeu.screen = pygame.display.set_mode((w, w))
    pygame.display.set_caption("Fenetre de jeu")
    donnee_jeu.clock = pygame.time.Clock()
    donnee_jeu.screen.fill((255, 255, 255))


def _fermer_fenetre():
    print("Fermer la fenetre")

    pygame.quit()
    sys.exit(0)


def _loop():
    assert donnee_jeu.clock is not None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _fermer_fenetre()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _fermer_fenetre()

    pygame.display.flip()
    donnee_jeu.clock.tick(30)


def _initialize() -> None:

    _ouvrir_fenetre()


if __name__ == "__main__":
    print("Ceci n'est pas un jeu.")
    sys.exit(1)
else:
    _initialize()
