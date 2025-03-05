from dataclasses import dataclass
import flet
'''
class Voto:
    def __init__(self, materia, punteggio, data, lode):
        if punteggio == 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = lode #è un bool
        elif punteggio < 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = False  # è un bool
        else:
            raise ValueError(f"Attenzione, lode non applicabile con voto uguale a {self.punteggio}") #funziona come throw new
    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"
'''

@dataclass #decoratore è una funzione che prende come argomento una classe, e restituisce un'altra classe
class Voto:
    materia: str #c'è il tipo, in fase di complilazione queste definizioni vengono ignorate, vengono messe solo per l'editor
    punteggio: int
    data: str
    lode: bool

    def __str__(self): # posso riusare i metodi definiti prima se voglio migliorare; la dataclass è molto utile perchè velocizza
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"


class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti
    def append(self, voto): #duck
        self.voti.append(voto)
    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario}"
        for v in self.voti:
            mystr += f"{v} \n" # dunder str del voto, delegation del metodo __str__ della classe Voto
        return mystr
    def __len__(self):
        return len(self.voti) #quanti elementi ha la lista voti, specializzo un comportamento
    def calcolaMedia(self):
        """
        restituisce la media dei voti attualmente presenti nel libretto
        :return: valore numerico della media, oppure ValueError nle caso in cui la lista fosse vuota
        """
        #media = sommaVoti / numeroEsami
        #v = []
        #for v1 in self.voti:
            #v1.append(v1.punteggio)
        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota")
        v = [v.punteggio for v in self.voti] #sintassi semplificata per ciclare nei voti e inserire nella lista i punteggi di ogni oggetto voto
        return sum(v) / len(v)
    def getVotiByPunti(self, punti, lode):
        """
        restituisce una lista di esami con punteggio uguale a punti ( e lode se assegnata)
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: booleano che indica se presente la lode
        :return: lista di voti
        """
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode: #se i nostri oggetti sono delle dataclass non serve implementare metodo __eq__
                votiFiltrati.append(v)
        return votiFiltrati
    def getVotoByName(self, nome):
        """
        restiuisce un oggetto Voto il cui campo materia è uguale a nome
        :param nome: stringa che indica il nome della materia
        :return: oggetto di tipo Voto, oppure None in caso di voto non trovato
        """
        for v in self.voti:
            if v.materia == nome:
                return v



def testVoto(): #in questo modo le variabili vengono distrutte alla fine del test, le varibaili sono localizzate e si creano solo se chiamo il metodo
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
    myLib = Libretto(None, [v1, v2])
    print(myLib)
    myLib.append(v3)
    print(myLib)


if __name__ == "__main__": #significa se sto eseguendo il main oppure solo questo blocco
    # dunder name può assumere dunder main oppure la rappresentazione stringa del modulo (in questo caso 'voto')
    #se vale __main__ vuol dire che lo sto eseguendo da solo
    testVoto()
