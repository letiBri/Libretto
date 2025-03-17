from view import View

class Controller:
    def __init__(self, v: View):
        self._view = v

    def handleAggiungi(self, e):
        strIn = self._view._txtIn.value
        if strIn == "":
            self._view._txtOut.value = "Errore: campo vuoto"
            self._view._page.update()
            return
        self._view._txtOut.value = strIn
        self._view._page.update()
