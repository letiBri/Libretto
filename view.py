import datetime

import flet as ft

class View:
    def __init__(self, page: ft.Page):
        self._btnPrint = None
        self._btnADd = None
        self._btnCal = None
        self._dp = None
        self._ddVoto = None
        self._txtInNome = None
        self._student = None
        self._titolo = None
        self._txtOut = None
        self._btnIn = None
        self._txtIn = None
        self._controller = None #per avere tutte le propoerties nell'init
        self._page = page #variabili che vorrei nessuno toccasse


    def loadInterface(self):
        """
        In questo metodo definiamo e carichiamo tutti i controlli dell'interfaccia
        :return:
        """
        self._titolo = ft.Text(value="Libretto voti", color="red", size=24)
        self._student = ft.Text(value=self._controller.getStudent(), color="brown")
        row1 = ft.Row(controls=[self._titolo], alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row(controls=[self._student], alignment=ft.MainAxisAlignment.END)


        self._txtInNome = ft.TextField(label="Nome esame", hint_text="Inserisci il nome dell'esame", width=300)
        self._ddVoto = ft.Dropdown(label="Voto", width=120)
        self._fillDDVoto()

        self._dp = ft.DatePicker(first_date=datetime.datetime(2022, 1, 1),
                                 last_date=datetime.datetime(2026, 12, 31),
                                 on_change=lambda e: print(f"Giorno selezionato: {self._dp.value}"),
                                 on_dismiss=lambda e: print("Data non selezionata"))

        self._btnCal = ft.ElevatedButton(text="Pick date", icon=ft.Icons.CALENDAR_MONTH, on_click=lambda _: self._page.open(self._dp))
        # si mette _ perchè tanto non usi l'argomento di input della funzione lambda, sarebbe una e

        self._btnADd = ft.ElevatedButton("Aggiungi", on_click=self._controller.handleAggiungi)
        self._btnPrint = ft.ElevatedButton("Stampa", on_click=self._controller.handleStampa)

        row3 = ft.Row(controls=[self._txtInNome, self._ddVoto, self._btnCal, self._btnADd, self._btnPrint], alignment=ft.MainAxisAlignment.CENTER)

        self._txtOut = ft.ListView(expand=True)

        self._page.add(row1, row2, row3, self._txtOut) # l'ordine con cui aggiungiamo è l'ordine con cui visuliazziamo


    def setController(self, c):
        self._controller = c


    def _fillDDVoto(self):
        for i in range(18, 30):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))
