#coding:utf-8
# === === Pioche === === #

from package.arriere import *
from package.carte import *
from package.champBataille import *
from package.cimetiere import *
from package.front import *
from package.joueur import *
from package.mainJoueur import *
from package.partie import *

from package.reserve import *
from package.royaume import *

def creerPioche(indice) :
    # Pre-condition : Int donné en parametre (indice) est un entier egal à 1 ou 2.
    # Post-condition : Aucune
    # Resultat : Créer un élément de Type Pioche dans laquelle il y aura : 9 cartes avec le Role = "Archer", 6 cartes avec Role = "Garde" et 5 cartes dont le Role = "Soldat". La fonction renvoie la pioche créée 
    pioche = []

    for i in range(8):
        pioche.append(creerCarte("Archer"))
    for i in range(5):
        pioche.append(creerCarte("Garde"))
    for i in range(4):
        pioche.append(creerCarte("Soldat"))
    return pioche

    

def piocher(pioche) : 
    # Pre-condition : pioche est de type Pioche
    # Post-condition : Aucune
    # Resultat : Renvoie une carte aléatoire dans la pioche donnée en parametre. La pioche est alors modifiée, la carte piochant etant retirée de la pioche.
    carte = choice(pioche) #prend une carte au hasard
    pioche.remove(carte)
    return carte
    
def ajouterPioche(pioche,carte) :
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : ajoute la carte donnée en paramètre dans la pioche donnée en parametre. Modife et renvoie la pioche modifiée
    pioche.append(carte)
    return pioche
    

def nbCartePioche(pioche) : 
    # Pre-condition : pioche est de type Pioche
    # Post-condition : Aucune
    # Resultat : Renvoie le nombre de carte restant dans la pioche entrée en paramètre
    return len(pioche)