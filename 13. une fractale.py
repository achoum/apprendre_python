from jeu import *


def ma_fractale(x1, y1, x2, y2, d):
    if d <= 0:
        dessiner_ligne(x1, y1, x2, y2)
        return

    dx = (x2-x1)//3
    dy = (y2-y1)//3

    mx = (x2-x1)//2 + x1 + dy
    my = (y2-y1)//2 + y1 - dx

    ma_fractale(x1, y1, x1+dx, y1+dy, d-1)
    ma_fractale(x1+dx, y1+dy, mx, my, d-1)
    ma_fractale(mx, my, x1+2*dx, y1+2*dy, d-1)
    ma_fractale(x1+2*dx, y1+2*dy, x2, y2, d-1)


while True:
    choisir_couleur(couleur_au_hasard())
    for d in range(8):
        effacer_ecran()
        ma_fractale(x1=0, y1=400, x2=800, y2=400, d=d)
        mettre_ecran_a_jour()
        attendre(seconds=0.5)
