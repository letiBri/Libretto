import flet as ft

class View:
    def __init__(self, page: ft.Page):
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
        self._txtIn = ft.TextField(label="Inserisci nome")
        self._btnIn = ft.ElevatedButton(text="Aggiungi", on_click=self._controller.handleAggiungi) 
        row = ft.Row(controls=[self._txtIn, self._btnIn])
        self._txtOut = ft.Text("")
        self._page.add(row, self._txtOut)

    def setController(self, c):
        self._controller = c
