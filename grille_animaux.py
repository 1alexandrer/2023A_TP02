from enum import Enum
import random

from simulation_constants import *
from animal import *


class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2


def creer_case(etat=Contenu.VIDE, animal=None):
    # TODO: Créer et retourner un dictionnaire représentant une case. Utiliser les arguments pour initialiser l'état et l'animal dans la case.
    
    case = {'etat' : etat, 'animal' :  animal} 
    
    return case


  




def creer_grille(nb_lignes, nb_colonnes):
    
    matrice = [[creer_case() for _ in range(nb_colonnes)] for _ in range(nb_lignes)]
            
    x = {"matrice" : matrice, "nb_proies": 0,
          "nb_predateurs": 0,
          "nb_lignes": nb_lignes,
          "nb_colonnes": nb_colonnes}
    return x
    # TODO: Créer une matrice 2D de cases vides et la retourner sous forme de dictionnaire
    # TODO: Dans le dictionnaire, ajouter des métadonnées décrites dans l'énoncé (nombre de proies, de prédateurs, etc.)
    
def obtenir_case(grille, ligne, colonne):
    case = grille['matrice'][ligne][colonne]
    return case
    pass

def obtenir_animal(grille, ligne, colonne):
    animal = grille['matrice'][ligne][colonne]['animal']
    return animal
    pass

def definir_animal(grille, animal, ligne, col):
    # TODO: Placer un animal (sous forme de dictionnaire) sur la case indiquée par les coordonnées (ligne, col).


    grille['matrice'][ligne][col]['animal'] = animal
    pass


def definir_case(grille, case, ligne, col):
    grille['matrice'][ligne][col] = case
    pass

    
    
def obtenir_population(grille):
    # TODO: Retourner un tuple contenant le nombre actuel de proies et de prédateurs dans la grille (Tuple[Int, Int])
    cntpred = 0
    cntprey = 0
    for x in range(len(grille['matrice'])):
        for y in range(len(grille['matrice'][x])):
            if grille['matrice'][x][y].get('etat') == Contenu.PROIE:
                cntprey += 1

            elif grille['matrice'][x][y].get('etat') == Contenu.PREDATEUR:
                cntpred += 1
            else:
                pass
                
    return (cntprey,cntpred)            
        

    pass


def obtenir_dimensions(grille):
    # TODO: Retourner un tuple avec le nombre de lignes et de colonnes de la grille (Tuple[Int, Int])
     
     nblign = 0
     nbcol= 0
     
     for x in range(len(grille['matrice'])):
        if x > nblign:
            nblign = x 
        for y in range(len(grille['matrice'][x])):
            if y > nbcol:
                nbcol = y

        
     return (nblign+1,nbcol+1)

    
    
    
    
    
    





def obtenir_animal(grille, ligne, col):
    # TODO: Retourner l'animal présent dans la case aux coordonnées données (ligne, col) (Dict)
    pass


def incrementer_nb_proies(grille):
    # TODO: Augmenter le compteur du nombre de proies dans la grille de 1 (Int)\
    grille['nb_proies'] += 1
    pass


def decrementer_nb_proies(grille):
    if grille['nb_proies'] != 0:
        grille['nb_proies'] -= 1
    pass


def incrementer_nb_predateurs(grille):
    # TODO: Augmenter le compteur du nombre de prédateurs dans la grille de 1 (Int)
     grille['nb_predateurs'] += 1
     pass


def decrementer_nb_predateurs(grille):
    # TODO: Diminuer le compteur du nombre de prédateurs dans la grille de 1 (Int)


    if grille['nb_predateurs'] != 0:
        grille['nb_predateurs'] -= 1
    pass
    pass


def check_nb_proies(grille, max_val):
    # TODO: Vérifier si le nombre actuel de proies dans la grille est inférieur à max_val (Booléen)
   
    if grille['nb_proies'] < max_val:
        return True
    else: 
        return False
   
   
   
    pass




def vider_case(grille, ligne, col):
    # TODO: Écraser la case située à la ligne et la colonne données avec une case vide
    case = creer_case()
    grille['matrice'][ligne][col] = case
    pass


def definit_etat(grille, etat, ligne, col):
    # TODO: Mettre à jour l'état de la case située à la ligne et la colonne données.
    # Utiliser le paramètre 'etat', qui est une valeur de l'Enum Contenu (VIDE, PROIE, PREDATEUR).
    pass


def definir_animal(grille, animal, ligne, col):
    # TODO: Placer un animal (sous forme de dictionnaire) sur la case indiquée par les coordonnées (ligne, col).
    pass


def obtenir_etat(grille, ligne, col):
    # TODO: Obtenir et retourner l'état actuel de la case à la position (ligne, col).
    # Le type de retour est une valeur de l'Enum Contenu (VIDE, PROIE, PREDATEUR).
    pass


def generer_entier(min_val, max_val):
    # TODO: Utiliser une librairie pour générer un nombre entier aléatoire entre min_val et max_val inclus.
    # Le résultat doit être un entier.
    pass


def ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col):

    lgnfix = lig%dim_lig
    colfix = col%dim_col

    return (lgnfix,colfix)

    

    # TODO: Ajuster la position (ligne, colonne) pour une grille circulaire en utilisant les dimensions de la grille.
    # Indice: Un modulo (%) peut être utile.
    pass


def choix_voisin_autour(grille, ligne, col, contenu: Contenu):
    # TODO: Chercher tous les voisins autour de la cellule (ligne, col) qui correspondent au "contenu" donné (Enum).
    # TODO: Renvoyer le nombre total de ces voisins, ainsi que les coordonnées d'un voisin choisi aléatoirement (Tuple).
    #       Si le contenu n'est pas VIDE, le voisin doit être disponible (voir la fonction obtenir_disponibilite).
    # Indice: Utiliser la fonction "ajuster_position_pour_grille_circulaire" pour ajuster les positions des voisins qui sont en dehors de la grille.
    count = 0
    position = []
    
    for x in range(ligne-1,ligne+2):
        for y in range(col-1,col+2):
            
            if x == ligne and y == col:
                pass
            else: 
                
                dimlign,dimcolg = obtenir_dimensions(grille)
                x,y = ajuster_position_pour_grille_circulaire(x,y,dimlign,dimcolg)
                
                
                if type(x) is int and type(y) is int and grille['matrice'][x][y]['etat'] == contenu:
                    
                    if contenu != Contenu.VIDE:
                        if obtenir_disponibilite(grille['matrice'][x][y]['animal']) == True:
                            count += 1
                            position.append([x,y])
                           

                    else:
                            count+=1
                            b = [x,y]
                            position.append([x,y])
                            
    if position == []:

        rdnlgn = None
        rdncol = None
    else:                      
        rnd = random.choice(position)    
        rdnlgn = rnd[0]           
        rdncol = rnd[1]    

                            

                            
     
      
    return count,rdnlgn,rdncol

                            



    
    
    pass






def remplir_grille(grille, pourcentage_proie, pourcentage_predateur):
    # TODO: Obtenir les dimensions de la grille.
    lgndim,coldim = obtenir_dimensions(grille)
    
    # TODO: Calculer le nombre total de cases dans la grille.
    nbttlcase = coldim * lgndim

    nbcsProie = round(nbttlcase*pourcentage_proie)
    nbcsPredateur = round(nbttlcase*pourcentage_predateur)
    # TODO: Calculer le nombre de proies à placer dans la grille.
    
    # TODO: Calculer le nombre de prédateurs à placer dans la grille.
    emptyArr = []
    # TODO: Générer et mélanger aléatoirement la liste de toutes les positions possibles.
    for x in range(lgndim):
        for y in range(coldim):
           
            emptyArr.append([x,y])
            

    
    randomlist = (random.sample(emptyArr, nbcsPredateur+nbcsProie))

    for x in range(nbcsProie):
        definir_animal(grille,creer_animal(random.randint(0,MAX_AGE_PROIE),NB_JRS_GESTATION_PROIE),randomlist[x][0],randomlist[x][1])
        incrementer_nb_proies(grille)
    # TODO: Placer les proies dans la grille.
    # Utilisez MAX_AGE_PROIE pour générer un âge aléatoire entre 0 et l'âge maximum de la proie.
    # Utilisez NB_JRS_GESTATION_PROIE et NB_JRS_PUBERTE_PROIE pour déterminer la période de gestation si la proie est en âge de procréer.
    
    # TODO: Mettre à jour le compteur du nombre de proies.
    for x in range(nbcsProie,nbcsPredateur+nbcsProie):
        definir_animal(grille,creer_animal(random.randint(0,MAX_AGE_PRED),NB_JRS_GESTATION_PROIE),randomlist[x][0],randomlist[x][1])
        incrementer_nb_predateurs(grille)
    # TODO: Placer les prédateurs dans la grille.
    # Utilisez MAX_AGE_PRED pour générer un âge aléatoire entre 0 et l'âge maximum du prédateur.
    # Utilisez NB_JRS_GESTATION_PRED et NB_JRS_PUBERTE_PRED pour déterminer la période de gestation si le prédateur est en âge de procréer.
    # Utilisez AJOUT_ENERGIE pour initialiser la quantité d'énergie du prédateur.
    
    # TODO: Mettre à jour le compteur du nombre de prédateurs.
    
    pass