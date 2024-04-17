import flet as ft
import libretto
from random import randint


class Controller(object):
    def __init__(self, view):
        self.view = view
        self._model = libretto.Libretto()
        self.startUpLibretto(10)

    def startUpLibretto(self, numero_esami:int):
        lst_esami = ['Analisi I', 'Analisi II', 'Fisica I',
                     'Fisica II', 'Chimica', 'Meccanica razionale', 'Informatica I'
            , 'Cucina creativa', 'Salsa baciacata', 'Astronomia', 'Letteratura classica', 'Musica I'
                     'Musica II', 'Stora Alto Medioevo', 'Biologia', 'Elettronica'
                     ]

        indici = set()
        while len(indici) != numero_esami:
            i = randint(0, len(lst_esami)-1)
            indici.add(i)

        for i in indici:
            nome_esame = lst_esami[i]
            crediti = randint(5, 15)
            punteggio = randint(18, 30)
            lode = True if punteggio == 30 and crediti % 2 == 0 else False
            data = f"{randint(2000, 2023)}-{randint(1, 12)}-{randint(1, 28)}"

            voto = libretto.Voto(nome_esame, crediti, punteggio, lode, data)

            self._model.append(voto)

    def _handleAdd(self, e):
        nome_esame = self.view.nome_esame.value

        pass
    def _handlePrint(self, e):
        self.view.lvElencoEsami.controls.clear()

        for esame in self._model.esami:
            self.view.lvElencoEsami.controls.append(  ft.Text(value= esame) )
        self.view.lvElencoEsami.update()
        pass
