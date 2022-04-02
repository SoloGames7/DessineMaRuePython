import turtle
from random import randint


def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    '''
    turtle.pendown()
    turtle.setpos(x, y)
    turtle.setpos(x+w, y)
    turtle.setpos(x+w, y+h)
    turtle.setpos(x, y+h)
    turtle.setpos(x, y)
    turtle.penup()


def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
    turtle.penup()
    turtle.setpos(x1, y1)
    turtle.pendown()
    turtle.setpos(x2, y2)
    turtle.penup()
    pass


def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre



    turtle.setpos(x, y)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.setpos(x+30, y)
    turtle.setpos(x+30, y+50)
    turtle.setpos(x, y+50)
    turtle.setpos(x, y)
    turtle.end_fill()
    turtle.penup()


    # balcon
    turtle.pensize(3)
    turtle.pendown()
    turtle.setpos(x-5, y)
    turtle.setpos(x-5, y+25)
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.setpos(x, y+25)
    turtle.penup()
    turtle.setpos(x+5, y)
    turtle.pendown()
    turtle.setpos(x+5, y+25)
    turtle.penup()
    turtle.setpos(x+10, y)
    turtle.pendown()
    turtle.setpos(x+10, y+25)
    turtle.penup()
    turtle.setpos(x+15, y)
    turtle.pendown()
    turtle.setpos(x+15, y+25)
    turtle.penup()
    turtle.setpos(x+20, y)
    turtle.pendown()
    turtle.setpos(x+20, y+25)
    turtle.penup()
    turtle.setpos(x+25, y)
    turtle.pendown()
    turtle.setpos(x+25, y+25)
    turtle.penup()
    turtle.setpos(x+30, y)
    turtle.pendown()
    turtle.setpos(x+30, y+25)
    turtle.penup()
    turtle.setpos(x+35, y)
    turtle.pendown()
    turtle.setpos(x+35, y+25)
    turtle.setpos(x-5, y+25)
    turtle.setpos(x-5, y)
    turtle.setpos(x+35, y)
    turtle.penup()
    turtle.pensize(1)


def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    turtle.penup()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.setpos(x, y+20)
    turtle.pendown()
    turtle.setpos(x+30, y+20)
    turtle.setpos(x+30, y+50)
    turtle.setpos(x, y+50)
    turtle.setpos(x, y+20)
    turtle.end_fill()
    turtle.penup()


def facade(x, y, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''

    turtle.penup()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.setpos(x, y+(60*niveau))
    turtle.pendown()
    turtle.setpos(x+140, y+(60*niveau))
    turtle.setpos(x+140, y+(60*niveau)+60)
    turtle.setpos(x, y+(60*niveau)+60)
    turtle.setpos(x, y+(60*niveau))
    turtle.end_fill()
    turtle.penup()


def porte(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    '''

    turtle.penup()
    turtle.fillcolor(couleur)
    turtle.begin_fill()

    turtle.setpos(x, y)
    turtle.pendown()
    turtle.setpos(x+30, y)
    turtle.setpos(x+30, y+50)
    turtle.setpos(x, y+50)
    turtle.setpos(x, y)




    turtle.end_fill()
    turtle.penup()


def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade

    facade(x,y_sol,c_facade,0)

    # Construit les 3 éléments (1 porte et 2 fenetres)

    a=randint(1,3)

    if a==1:
        porte(x+15 ,y_sol,c_porte)
        fenetre(x+55,y_sol)
        fenetre(x+95,y_sol)

    if a==2:
        fenetre(x+15,y_sol)
        porte(x+55 ,y_sol,c_porte)
        fenetre(x+95,y_sol)

    if a==3:
        fenetre(x+15,y_sol)
        fenetre(x+55,y_sol)
        porte(x+95 ,y_sol,c_porte)


def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs

    facade(x , y_sol , couleur , niveau)

    # dessin des 3 Eléments

    a=randint(1,3)

    if a==1:
        fenetre_balcon(x+15 ,y_sol+(niveau*60))
        fenetre(x+55,y_sol+(niveau*60))
        fenetre(x+95,y_sol+(niveau*60))

    if a==2:
        fenetre(x+15,y_sol+(niveau*60))
        fenetre_balcon(x+55 ,y_sol+(niveau*60))
        fenetre(x+95,y_sol+(niveau*60))

    if a==3:
        fenetre(x+15,y_sol+(niveau*60))
        fenetre(x+55,y_sol+(niveau*60))
        fenetre_balcon(x+95 ,y_sol+(niveau*60))


def couleur_aleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''
    r=randint(0,255)
    if r<100:
        r="0"+str(r)
        r=int(r)
    v=randint(0,255)
    if v<100:
        v="0"+str(v)
        v=int(v)
    b=randint(0,255)
    if b<100:
        b="0"+str(b)
        b=int(b)

    return (r,v,b)


# ----- Sol de la rue -----
def sol(y_sol):
    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''

    trait(-960,y_sol,960,y_sol)


def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    turtle.fillcolor("black")
    turtle.begin_fill()
    trait(x-10, y_sol+((niveau+1)*60), x+150, y_sol+((niveau+1)*60))
    trait(x+150, y_sol+((niveau+1)*60), x+70, y_sol+((niveau+1)*60)+40)
    trait(x+70, y_sol+((niveau+1)*60)+40, x-10, y_sol+((niveau+1)*60))
    turtle.end_fill()


def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.fillcolor("black")
    turtle.begin_fill()
    trait(x, y_sol+((niveau+1)*60), x+140, y_sol+((niveau+1)*60))
    turtle.pendown()
    turtle.circle(5, 180)
    turtle.penup()
    trait(x+140, y_sol+((niveau+1)*60)+10, x, y_sol+((niveau+1)*60)+10)
    turtle.pendown()
    turtle.circle(5, 180)
    turtle.penup()
    turtle.end_fill()


def toit(x, y_sol, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Cette fonction dessine au hasard un des 2 types de toit

    '''
    a=randint(1,2)
    if a==1:
        toit1(x,y_sol,niveau)
    if a==2:
        toit2(x,y_sol,niveau)




def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    # Nombre d'étage (aléatoire)

    nbet = randint(0,4)

    #Couleurs des éléments (aléatoire)
    coulPorte = couleur_aleatoire()
    couBat = couleur_aleatoire()
    # Dessin du RDC

    rdc(x, y_sol ,couBat , coulPorte)

    # Dessin des étages
    if nbet!= 0:
        for i in range(1,nbet+1):
            etage(x,y_sol ,couBat , i)

    # Dessin du toit
    toit(x,y_sol,nbet)


def ciel(y_sol):
    turtle.fillcolor(18, 196, 255)
    turtle.begin_fill()
    turtle.setpos(-960,y_sol)
    turtle.pendown()
    turtle.setpos(960,y_sol)
    turtle.setpos(960,y_sol+(-y_sol)+540)
    turtle.setpos(-960,y_sol+(-y_sol)+540)
    turtle.setpos(-960,y_sol)
    turtle.penup()
    turtle.end_fill()

def terre(y_sol):
    turtle.fillcolor(96, 112, 117)
    turtle.begin_fill()
    turtle.setpos(-960,y_sol)
    turtle.pendown()
    turtle.setpos(960,y_sol)
    turtle.setpos(960,y_sol+(-y_sol)-540)
    turtle.setpos(-960,y_sol+(-y_sol)-540)
    turtle.setpos(-960,y_sol)
    turtle.penup()
    turtle.end_fill()

def decor(y_sol):
    ciel(y_sol)
    terre(y_sol)

##if __name__ == '__main__':
##    ciel(-200)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    immeuble(0,0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##
##if __name__ == '__main__':
##    toit(0,0,0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()


##if __name__ == '__main__':
##    toit2(0,0,0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()


##if __name__ == '__main__':
##    toit1(0,0,0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    sol(0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    etage(0,0,"red",0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    rdc(0,0,"red","green")
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    porte(0,0,"red")
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    facade(0,0,"red",0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    fenetre(0,0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    fenetre_balcon(0,0)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()

##if __name__ == '__main__':
##    rectangle(0,0,150,100)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()


##if __name__ == '__main__':
##    trait(0,0,100,100)
##    # On ferme la fenêtre s'il y a un clique gauche
##    turtle.exitonclick()



