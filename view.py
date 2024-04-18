#from controller import Controller
import datetime

import flet as ft
class View(object):
    def __init__(self, page:ft.Page):
        self._page = page
        self._page.window_width = 700  # window's width is 200 px
        self._page.window_height = 600
        self._page.horizontal_alignment=ft.MainAxisAlignment.CENTER


        self._controller = None

        self.nome_esame = None
        self.cfu = None
        self.ddPuntegggio = None

        self.datePicker = None
        self.lvElencoEsami = None
        self.lblDataEsame = None

        self.dlg_modal = ft.AlertDialog(
            modal=True,

            actions=[
                ft.TextButton("OK", on_click=self.close_dlg),

            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
    def carica_interfaccia(self):
        colonna = ft.Column([], alignment=ft.MainAxisAlignment.CENTER)
        # riga 1
        lbltitolo = ft.Text("Il mio libretto voti", color='blue',
                               size=24, text_align=ft.TextAlign.CENTER)

        riga1 = ft.Row([lbltitolo], alignment=ft.MainAxisAlignment.CENTER)


        # riga2
        self.lblDataEsame = ft.Text('data', text_align=ft.TextAlign.CENTER)
        self.nome_esame = ft.TextField(label='nome esame', width=200, text_size=12)
        self.cfu = ft.TextField(label='CFU', width=100, text_size=12)
        self.ddPuntegggio = ft.Dropdown(options=[], label='voto', width=100, text_size=12)
        for punteggio in range(18, 31):
            self.ddPuntegggio.options.append(ft.dropdown.Option(str(punteggio)))
        self.ddPuntegggio.options.append(ft.dropdown.Option('30L'))

        self.datePicker = ft.DatePicker(
            on_change=self.change_date,
            on_dismiss=self.date_picker_dismissed,
            first_date=datetime.datetime(2020,1,1),
            last_date=datetime.datetime(2024,1,1)
        )
        self._page.overlay.append(self.datePicker)

        btnCalendario = ft.ElevatedButton(text='Data', icon=ft.icons.CALENDAR_MONTH,
                                          on_click=lambda _: self.datePicker.pick_date())

        riga2 = ft.Row([self.nome_esame, self.cfu, self.ddPuntegggio, btnCalendario, self.lblDataEsame], alignment=ft.MainAxisAlignment.CENTER)

        # riga3
        btnAdd = ft.ElevatedButton(text='Add', on_click=self.handleAdd)
        btnPrint = ft.ElevatedButton(text='Print', on_click=self._controller._handlePrint)
        riga3 = ft.Row([btnAdd, btnPrint], alignment=ft.MainAxisAlignment.CENTER)

        # riga 4
        self.lvElencoEsami = ft.ListView(auto_scroll=True)

        colonna.controls.append(riga1)
        colonna.controls.append(riga2)
        colonna.controls.append(riga3)
        colonna.controls.append(self.lvElencoEsami)

        self._page.add(colonna)

    def controllaCampi(self):

        if self.nome_esame.value == '':
            self.dlg_modal.title = ft.Text('ATTENZIONE - Nome esame')
            self.dlg_modal.content=ft.Text("Il campo nome esame deve essere riempito")
            self._page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            self._page.update()
            self.nome_esame.focus()
            return False

        if self.ddPuntegggio.value == None:
            self.dlg_modal.title = ft.Text('ATTENZIONE - punteggio')
            self.dlg_modal.content = ft.Text("Il campo punteggio deve essere selezionato")
            self._page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            self._page.update()
            self.ddPuntegggio.focus()
            return False

        return  True

    def handleAdd(self, e):
        if  self.controllaCampi():
           self._controller._handleAdd()


    def close_dlg(self, e):
        self.dlg_modal.open = False
        self._page.update()


    def setController(self, c):
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
    def change_date(self, e):
        #print(f"Date picker changed, value is {self.datePicker.value}")

        data = self.datePicker.value
        if data != None:
            self.lblDataEsame.value = f"{data.day}/{data.month}/{data.year}"

        else:
            self.lblDataEsame.value=''
        self.lblDataEsame.update()

    def date_picker_dismissed(self, e):
        #data = self.datePicker.value

        #print(f"Date picker dismissed, value is {self.datePicker.value}")
        pass