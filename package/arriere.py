#coding:utf-8
# === === Arriere === === #
import carte
def creerArriere() :
    # Pre-condition : Aucune
    # Post-condition : Aucune
    # Resultat : Créer un element de Type Arriere
    return {"A1" : "Vide", "A2" : "Vide", "A3" : "Vide"}

def envoyerArriere(arriere,carte,pos) :
    # Pre-condition : arriere est de type Arriere, carte est de type Carte. pos est un string dont le premier caractère est un A et le deuxieme est un chiffre
    # Post-condition : Aucune 
    # Resultat : La carte donnée en parametre est positionné dans l'arriere, à la position pos. La fonction modifie donc l'arriere et le renvoie
    carte.setPositionCarte(carte,pos)
    return arriere[pos] = carte

def nbCarteArriere(arriere) : 
    # Pre-condition : arriere est de type Arriere
    # Post-condition : Aucune 
    # Resultat : Indique le nombre de carte présente sur l'arriere 
    nbCarte = 0
    if arriere["A1"] != "Vide" :
	nbCarte = nbCarte + 1
    if arriere["A2"] != "Vide" :
	nbCarte = nbCarte + 1 
    if arriere["A3"] != "Vide" :
	nbCarte = nbCarte + 1
    return nbCarte 

def extraireArriere(arriere,pos) : 
    # Pre-condition : arriere est de type Arriere, pos est un str 
    # Post-condition : Aucune 
    # Resultat : renvoie la carte située à la position pos, et modifie l'arriere en retirant la carte. 
    res = arriere[pos]
    setPositionCarte(arriere[pos],"Vide")
    arriere[pos] = "Vide"
    return res 
