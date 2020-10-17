'''
Created on 17 oct. 2020

@author: paradoxisme
'''
import random


class Serveur(object):
    def __init__(self):
        self._clients = []
        self._clef = 0
        self._cumule_vote = 1

    def connect_client(self, new_client):
        self._clients.append(new_client)

    def melanger_clef(self):
        for client in self._clients:
            copie_liste = self._clients.copy()
            random.shuffle(copie_liste)
            for _ in range(client.part_num):
                client.echange_parties(copie_liste.pop())

    def envoyer_clef(self, clef):
        self._clef ^= clef

    def envoyer_vote(self, vote):
        self._cumule_vote ^= vote

    @property
    def resultat(self):
        return self._cumule_vote ^ self._clef
