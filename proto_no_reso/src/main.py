'''
Created on 17 oct. 2020

@author: paradoxisme
'''
from serveur import Serveur
from votant import Votant
import random


def main():
    serveur = Serveur()
    votants = [Votant(serveur, 5) for _ in range(50)]
    serveur.melanger_clef()
    vote_nom_index = random.randrange(100)
    tout_oui = True
    for i, votant in enumerate(votants):
        if i != vote_nom_index:
            votant.vote_oui()
        else:
            votant.vote_non()
            tout_oui = False
    print(tout_oui)
    print(serveur.resultat)


if __name__ == '__main__':
    for _ in range(100):
        main()
