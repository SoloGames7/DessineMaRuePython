import turtle
from random import randint, shuffle
from fonctions_rue import sol
from fonctions_rue import immeuble
from fonctions_rue import decor
# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(800, 600)
    turtle.speed(0)
    turtle.colormode(255)
    nbim=8

    # On définit la hauteur du sol
    y_sol = -200

    # Dessin du sol de la rue
    sol(y_sol)

    #
    decor(y_sol)

    # Dessin des 4 immeubles
    if (nbim*175)%2==0:
        x=-(nbim*175)/2
    else:
        x=-(nbim*175)+1

    for i in range(nbim):
        immeuble(x,y_sol)
        x+=175

    turtle.hideturtle()
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main()