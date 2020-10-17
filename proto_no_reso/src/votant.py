'''
Created on 17 oct. 2020

@author: paradoxisme
'''
import random
from functools import reduce


TAILLE_CLEF = 2**32


class Votant(object):
    """ Votant
    """
    def __init__(self, serveur, part_num=2):
        self._parties = [random.randrange(TAILLE_CLEF) for _ in
                         range(part_num)]
        self._vote_oui = reduce(lambda a, b: a ^ b, self._parties)
        self._vote = None
        serveur.connect_client(self)
        self._serveur = serveur

    @property
    def part_num(self):
        return len(self._parties)

    def echange_parties(self, autre_votant):
        partie_send = self._parties.pop()
        autre_votant.combine(partie_send)

    def combine(self, partie_ext):
        clef_temporaire = random.randrange(TAILLE_CLEF)
        clef_envoyer = clef_temporaire ^ partie_ext
        self._serveur.envoyer_clef(clef_envoyer)
        self._vote_oui ^= clef_temporaire

    def vote_oui(self):
        self._vote = self._vote_oui
        self._vote_oui = None
        self._serveur.envoyer_vote(self._vote)

    def vote_non(self):
        self._vote = random.randrange(TAILLE_CLEF)
        self._vote_oui = None
        self._serveur.envoyer_vote(self._vote)
