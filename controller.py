from view import View
import Libretto
from random import randint
from itertools import permutations

class Controller(object):
    def __init__(self, view:View):
        self.view = view
        self._model = Libretto.Libretto()
        self.startUpLibretto()

    def startUpLibretto(self, numero_esami:int):
        lst_esami = ['Analisi I', 'Analisi II', 'Fisica I',
                     'Fisica II', 'Chimica', 'Meccanica razionale', 'Informatica I'
            , 'Cucina creativa', 'Salsa baciacata', 'Astronomia', 'Letteratura classica', 'Musica I'
                     'Musica II', 'Stora Alto Medioevo', 'Biologia', 'Elettronica'
                     ]

        perm = permutations(iterable=lst_esami, r=numero_esami)
        perm = list(perm)
        i = randint(0, len(perm))
        nomi_esami = perm[i]

        for nome_esame in nomi_esami:

            crediti = randint(5, 15)
            punteggio = randint(18, 30)
            lode = True if punteggio == 30 and crediti % 2 == 0 else False
            data = f"{randint(2000, 2023)}-{randint(1, 12)}-{randint(1, 28)}"

            voto = Libretto.Voto(nome_esame, crediti, punteggio, lode, data)

            self._model.append(voto)

