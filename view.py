from controller import Controller
import flet as ft
class View(object):
    def __init__(self, page:ft.Page):
        self._page = page
        self._controller = None

    def setController(self, c:Controller):
        self._controller = c

    def menuCLI(self):
        titolo = "Gestione libretto"
        print()
        print(titolo)
        print(len(titolo)*'-')
        print("1. Visualizza Esami")
        print("2. Aggiungi Esame")
        print("3. Cerca esame")
        print("3. Calcola media")
        print("0. Esci\n")
