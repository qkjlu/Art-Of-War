#coding:utf-8
# === === Partie === === #

from package.arriere import *
from package.carte import *
from package.champBataille import *
from package.cimetiere import *
from package.front import *
from package.joueur import *
from package.mainJoueur import *

from package.pioche import *
from package.reserve import *
from package.royaume import *
    
def creerPartie(joueur1,joueur2) : 
    # Pre-condition : joueur1 et joueur2 sont de type Joueur
    # Post-condition : Aucune
    # Resultat : Retourne une partie dans laquelle : le premier joueur donné en paramètre est le joueurCourant et le deuxieme est son joueur adverse
    return { "joueurCourant" : joueur1, "joueurAdverse" : joueur2 }
    
    
def joueurCourant(partie) : 
    # Pre-condition : partie est de type Partie
    # Post-condition : Aucune
    # Resultat : Retourne le joueurCourant de la Partie
    return partie[joueurCourant] 
    

def joueurAdverse(partie) : 
    # Pre-condition : partie est de type Partie
    # Post-condition : Aucune
    # Resultat : Retourne un element Joueur qui est le Joueur Adverse du joueur courant de la partie donnée en paramètre.
    return partie[joueurAdverse]
    

def setJoueurCourant(joueur,partie) :
    # Pre-condition : joueur est de type Joueur, partie est de type Partie
    # Post-condition : Aucune
    # Resultat : Modifie la partie pour que le nouveau joueur courant soit celui entré en parametre. La fonction renvoie aussi la partie
    partie["joueurCourant"]=joueur
     
def setJoueurAdverse(joueur,partie) :
    # Pre-condition : joueur est de type Joueur, partie est de type Partie
    # Post-condition : Aucune
    # Resultat : Modifie la partie pour que le nouveau joueur adverse soit celui entré en parametre. La fonction renvoie aussi la partie
    partie["joueurAdverse"]=joueur


def changeJoueurCourant(partie) :
    # Pre-condition : partie est de type Partie
    # Post-condition : Aucune
    # Resultat : En utilisant setJoueurCourant, cette fonction modifie la partie : Le joueur adverse du joueur courant devient joueur courant. Renvoie aussi la Partie. 
    joueurCourant=joueurCourant(partie)
    setJoueurCourant(joueurAdverse(partie),partie)
    setJoueurAdverse(joueurCourant,partie)
    return partie
    
        
