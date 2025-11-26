import pygame
from pygame import Color

class Objet:

    def __init__(self, rectangle,vitesse,fenetre):
        self.r = rectangle
        self.v = vitesse
        self.f = fenetre
        self.actif = True

    def deplacer(self):    

        self.r.y = self.r.y + self.v
        if self.r.y > self.f.get_height():#Pour redessiner en haut
            self.actif = False

class Chapeau(Objet):

    def dessiner(self):

        if self.actif == True:
            pygame.draw.line(self.f, Color('red'),(self.r.x,self.r.y+self.r.height),(self.r.x+self.r.width, self.r.y+self.r.height),int(self.r.height/10))#bord du chapeau
            pygame.draw.polygon(self.f, Color('red'),((self.r.x,self.r.y),(self.r.x+self.r.width, self.r.y),(self.r.x+self.r.width/10*8, self.r.y+self.r.height),(self.r.x+self.r.width/10*2,self.r.y+self.r.height)))#haut du chapeau

class Tete(Objet):

    def dessiner(self):

        if self.actif == True:

            pygame.draw.ellipse(self.f, Color('white'), ((self.r.x,self.r.y), (self.r.width, self.r.height))) #tete
            pygame.draw.ellipse(self.f, Color('black'), ((self.r.x+self.r.width/110*35,self.r.y+self.r.height/110*40), (self.r.width/11, self.r.height/11))) #oeil gauche
            pygame.draw.ellipse(self.f, Color('black'), ((self.r.x+self.r.width/110*75,self.r.y+self.r.height/110*40), (self.r.width/11, self.r.height/11))) #oeil droit
            pygame.draw.polygon(self.f, Color('orange'),((self.r.x+self.r.width/110*55,self.r.y+self.r.height/110*60),(self.r.x+self.r.width/110*55, self.r.y+self.r.height/110*75),(self.r.x+self.r.width/110*85, self.r.y+self.r.height/110*68))) #nez

class Milieu(Objet):

    def dessiner(self):

        if self.actif == True:

            pygame.draw.ellipse(self.f, Color('white'), ((self.r.x,self.r.y), (self.r.width, self.r.height))) #haut du corps
            pygame.draw.ellipse(self.f, Color('black'), ((self.r.x+self.r.width/130*55,self.r.y+self.r.height/130*40), (self.r.width/130*15, self.r.height/130*15))) #bouton haut
            pygame.draw.ellipse(self.f, Color('black'), ((self.r.x+self.r.width/130*55,self.r.y+self.r.height/130*80), (self.r.width/130*15, self.r.height/130*15))) #bouton bas

class Bas(Objet):

    def dessiner(self):

        if self.actif == True :

            pygame.draw.ellipse(self.f, Color('white'), ((self.r.x, self.r.y), (self.r.width, self.r.height)))

class BrasDroit(Objet):

    def dessiner(self):

        if self.actif == True:

            pygame.draw.line(self.f, Color('brown'), (self.r.x, self.r.y+self.r.height),(self.r.x+self.r.width, self.r.y+self.r.height/90*10),int(self.r.width/80*10))
            pygame.draw.line(self.f, Color('brown'), (self.r.x+self.r.width/80*55, self.r.y+self.r.height/90*35),(self.r.x+self.r.width/80*55,self.r.y),int(self.r.width/80*10))


class BrasGauche(Objet):

    def dessiner(self):
        
        if self.actif == True:
            pygame.draw.line(self.f, Color('brown'), (self.r.x,self.r.y), (self.r.x+self.r.width, self.r.y+self.r.height),int(self.r.width/65*10))
            pygame.draw.line(self.f, Color('brown'), (self.r.x+self.r.width/65*25, self.r.y+self.r.height/80*30),(self.r.x+self.r.width/65*35, self.r.y-self.r.height/80*10),int(self.r.width/65*10))

class Palette:
    def __init__ (self, fenetre, x, y, largeur, hauteur, vitesse):
        self.f=fenetre
        self.x = x
        self.y = y
        self.l = largeur
        self.h = hauteur
        self.v = vitesse

    def rect(self):
        return pygame.Rect(self.x, self.y, self.l, self.h)
    
    def deplacer_clavier(self):
        touche = pygame.key.get_pressed()
        if touche [pygame.K_LEFT]:
            self.x -= self.v
        if touche [pygame.K_RIGHT]:
            self.x += self.v

    def deplacer_souris(self):
        if pygame.mouse.get_pressed()[0]:  # clic gauche enfoncé
            souris_x, _ = pygame.mouse.get_pos()
            self.x = souris_x - self.l // 2

    
    def appliquer_limites(self, largeur_fenetre):
        if self.x < 0:
            self.x = 0
        if self.x + self.l > largeur_fenetre:
            self.x = largeur_fenetre - self.l

    def dessiner(self):
        pygame.draw.rect(self.f, Color('white'), self.rect()) 