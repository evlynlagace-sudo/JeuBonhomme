import ClasseObjet as ClasseObjet
import random
import pygame
from pygame import Color

LARGEUR_JEU = 650
LARGEUR_PANNEAU=150
HAUTEUR_FENETRE = 600

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR_JEU+LARGEUR_PANNEAU, HAUTEUR_FENETRE))
pygame.display.set_caption('Dessiner Monsieur Frette !')

pygame.mixer.init()

def loader_fichiers_son(fichier_son):
    try:
        return pygame.mixer.Sound(fichier_son)
    except Exception:
        return None

#Les fichiers de sons
son_dessine = loader_fichiers_son("337049__shinephoenixstormcrow__320655__rhodesmas__level-up-01.mp3")
son_efface = loader_fichiers_son("676811__cogfirestudios__collect-game-pixel-lose.wav")
son_succes = loader_fichiers_son("740760__soundbitersfx__santa-claus-ho-ho-ho-merry-christmas.wav")
son_echec = loader_fichiers_son("394897__funwithsound__failure-4.wav")

def loader_images(fichier_image):
    try:
        return pygame.image.load(fichier_image)
    except Exception:
        return None
#Les images
image_reussite = loader_images("two-snowman-standing-together.png")
image_echec = loader_images("melting-snowman.png")

#Les zones d'affichage
zonePaneau = pygame.Surface((LARGEUR_PANNEAU, HAUTEUR_FENETRE))
zonePaneau.fill(Color('grey'))
zonePaneau_x=LARGEUR_JEU
zonePaneau_y=0

zoneJeu = pygame.Surface((LARGEUR_JEU, HAUTEUR_FENETRE))
zoneJeu.fill(Color('black'))
zoneJeu_x = 0
zoneJeu_y = 0

# La palette
pal_largeur = 50
pal_hauteur = 10
pal_x = (LARGEUR_JEU - pal_largeur) // 2   # centré
pal_y = HAUTEUR_FENETRE - pal_hauteur - 10     # en bas, marge de 10 px
palVitesse = 5

#pour dessiner la palette
palette1 = ClasseObjet.Palette(zoneJeu, pal_x, pal_y, pal_largeur,pal_hauteur,palVitesse)

#L'horloge et la vitesse a laquelle les objets tombent
horloge = pygame.time.Clock()
vitesse = 5

def nouvelObjet() :
    choix = random.randint(1,6)
    
    match choix:
        case 1 :
            rectangle =pygame.Rect(random.randint(0, LARGEUR_JEU-50),0,55,55)
            return ClasseObjet.Tete(rectangle, vitesse, zoneJeu)
        case 2 :
            rectangle =pygame.Rect(random.randint(0, LARGEUR_JEU-60),0,60,30)
            return ClasseObjet.Chapeau(rectangle, vitesse, zoneJeu)
        case 3 :
            rectangle =pygame.Rect(random.randint(0, LARGEUR_JEU-65),0,65,65)
            return ClasseObjet.Milieu(rectangle, vitesse, zoneJeu)
        case 4 :
            rectangle =pygame.Rect(random.randint(0, LARGEUR_JEU-80),0,80,80)
            return ClasseObjet.Bas(rectangle, vitesse, zoneJeu)
        case 5 :
            rectangle =pygame.Rect(random.randint(0, LARGEUR_JEU-80),0,45,40)
            return ClasseObjet.BrasDroit(rectangle, vitesse, zoneJeu)
        case 6 :
            rectangle =pygame.Rect(random.randint(0, LARGEUR_JEU-80),0,32,40)
            return ClasseObjet.BrasGauche(rectangle, vitesse, zoneJeu)

#Liste des objets qui tombent - un seul présentement
listeObjets = []
listeObjets.append(nouvelObjet())

#Liste des objets pour dessiner le bonhomme dans le panneau de droite :
chapeau_panneau = ClasseObjet.Chapeau(pygame.Rect(38,195,60,25),0,zonePaneau)
chapeau_panneau.actif=False
tete_panneau = ClasseObjet.Tete(pygame.Rect(40,215,55,55),0,zonePaneau)
tete_panneau.actif=False #pour ne pas dessiner au départ
milieu_panneau = ClasseObjet.Milieu(pygame.Rect(35,270,65,65),0,zonePaneau)
milieu_panneau.actif=False
bas_panneau = ClasseObjet.Bas(pygame.Rect(28,335,80,80), 0, zonePaneau)
bas_panneau.actif=False
bras_droit_panneau = ClasseObjet.BrasDroit(pygame.Rect(95,260,40,45),0,zonePaneau)
bras_droit_panneau.actif=False
bras_gauche_panneau = ClasseObjet.BrasGauche(pygame.Rect(10,260,30,45),0,zonePaneau)
bras_gauche_panneau.actif=False

#La tête doit être dessinée avant le chapeau pour que ce dernier se superpose correctement
listeObjetsPanneau = [tete_panneau, chapeau_panneau, milieu_panneau, bas_panneau, bras_droit_panneau, bras_gauche_panneau]

#Fonctions pour gérer l'affichage et le son 
def contenuPaneau(zonePaneau,objetPanneau):
 
    zonePaneau.fill(Color('grey'))

    for obj in objetPanneau:
        if obj.actif == True:
            obj.dessiner()

def rafraichirAffichage(compteur_oups):
        fenetre.blit(zoneJeu, (zoneJeu_x, zoneJeu_y))
        fenetre.blit(zonePaneau, (zonePaneau_x, 0))
        afficherCompteur(zonePaneau, compteur_oups)
        pygame.display.flip()


def afficherCompteur(zonePaneau, compteur):
    zonePaneau.fill(Color('grey'), (10,10,120,40)) #pour effacer le texte deja ecrit
    font = pygame.font.SysFont(None, 36)
    texte = font.render("Oups : "+str(compteur), True, Color('red'))
    zonePaneau.blit(texte,(10,10))

def afficherTexteFin(zoneJeu, texteFin):
    font =  pygame.font.SysFont(None, 48)
    texte = font.render(texteFin, True, Color('red'))
    zoneJeu.blit(texte,(10, 450))

def jouersonFin(fichier_son):
    if fichier_son is None:
        return
    try :
        fichier_son.play()
        while pygame.mixer.get_busy():
            pygame.time.delay(5)
    except Exception as e:
        print("erreur avec le fichier de son : ",e)            

def jouerson(fichier_son):
    if fichier_son is None:
        return
    try :
        fichier_son.play()
    except Exception as e:
        print("erreur avec le fichier de son : ",e)

#Fonctions pour gérer le jeu en tant que tel
def attendre_rejouer():
    font = pygame.font.SysFont(None, 48)
    texte = font.render("Rejouer ? Y/N", True, Color('red'))
    zoneJeu.blit(texte, (200, 500))
    rafraichirAffichage(compteur_oups)  # mettre à jour l'affichage pour montrer le texte

    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # touche Y
                    attente = False
                    jeu()
                elif event.key == pygame.K_n:  # touche N
                    pygame.quit()
                    exit()

def jeu ():

    #Le compteur
    global compteur_oups
    compteur_oups = 0 #reinitialiser le compteur à chaque partie

    for obj in listeObjetsPanneau: # remettre les objets dans le panneau à False à chaque début de partie
        obj.actif = False

    zonePaneau.fill(Color('grey'))

    #Pour animer
    fin = False

    while not fin :

        #Vérifier si le bonhomme est dessiné, et si oui arrêter le jeu
        if all(obj.actif for obj in listeObjetsPanneau):
            zoneJeu.fill(Color('white'))
            if image_reussite:
                zoneJeu.blit(image_reussite,(0,0))
                texte_reussite = "Félicitation !!!"
                afficherTexteFin(zoneJeu, texte_reussite)
            rafraichirAffichage(compteur_oups)
            jouersonFin(son_succes)
            attendre_rejouer()
            return

        #Vérifier si 5 morceaux manqués (pas attrapés et pas dessiné)    
        if compteur_oups>=5:
            zoneJeu.fill(Color('white'))
            if image_echec:
                zoneJeu.blit(image_echec,(0,0))
                texte_echec="Oupss... dommage !"
                afficherTexteFin(zoneJeu, texte_echec)

            rafraichirAffichage(compteur_oups)
            jouersonFin(son_echec)
            attendre_rejouer()
            return         

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            fin=True
        else :
            objet1 = listeObjets[0]
            objet1.deplacer()
            pygame.draw.rect(zoneJeu, Color('black'), (0, 0, LARGEUR_JEU, HAUTEUR_FENETRE))

            objet1.dessiner()

            # Pour déplacer la palette
            palette1.deplacer_clavier()
            palette1.deplacer_souris()
            palette1.appliquer_limites(LARGEUR_JEU)

            palette1.dessiner()

            #Quelle est la classe du morceau qui tombe -> indice dans la liste des objets du panneau
            if isinstance(objet1,ClasseObjet.Tete): # Il faut dessiner la tête avant le chapeau pour que le bonhomme s'affiche correctement !
                indice_morceau=0
            elif isinstance(objet1, ClasseObjet.Chapeau):
                indice_morceau=1
            elif isinstance(objet1, ClasseObjet.Milieu):
                indice_morceau=2
            elif isinstance (objet1, ClasseObjet.Bas):
                indice_morceau=3
            elif isinstance(objet1, ClasseObjet.BrasDroit):
                indice_morceau=4
            else :
                indice_morceau=5

            #verification des collisions
            if objet1.actif and objet1.r.colliderect(palette1.x, palette1.y, palette1.l, palette1.h):
                #si collision et l'objet n'est pas dessiné
                if listeObjetsPanneau[indice_morceau].actif == False:
                    jouerson(son_dessine)

                #si collision et l'objet est déjà dessiné    
                else :
                    jouerson(son_efface)
                    compteur_oups = compteur_oups + 1
                    rafraichirAffichage(compteur_oups)

                #pour dessiner, ou effacer, dans le panneau à droite l'objet attrapé
                listeObjetsPanneau[indice_morceau].actif = not listeObjetsPanneau[indice_morceau].actif
                contenuPaneau(zonePaneau,listeObjetsPanneau)

                #pour créer un nouvel objet qui va tomber après un morceau attrapé
                objet1.actif = listeObjets.pop()
                listeObjets.append(nouvelObjet())          

            #Pour vérifier que l'indice de la piece dans le tableau des objets du panneau existe
            piece_active = listeObjetsPanneau[indice_morceau].actif

            # Objet tombé sans être attrapé augmente le compteur des erreur
            if objet1.r.y + objet1.r.height >= HAUTEUR_FENETRE and not piece_active:
                compteur_oups = compteur_oups + 1          
                rafraichirAffichage(compteur_oups)

                #pour créer un nouvel objet après un morceau qui n'a pas été attrapé
                objet1.actif = listeObjets.pop()
                listeObjets.append(nouvelObjet())

            #pour faire tomber le prochain morceau
            if not objet1.actif :
                objet1.actif = listeObjets.pop()
                listeObjets.append(nouvelObjet())         

            rafraichirAffichage(compteur_oups)

            horloge.tick(60)
        pygame.display.flip()

jeu() # Pour lancer la première partie