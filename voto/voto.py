from dataclasses import dataclass


@dataclass(order=True) #decoratore è una funzione che prende come argomento una classe, e restituisce un'altra classe
#order=True userebbe i metodi basi lt, eq definiti da python per l'ordinamneto, noi non vogliamo questo
class Voto:
    materia: str #c'è il tipo, in fase di complilazione queste definizioni vengono ignorate, vengono messe solo per l'editor
    punteggio: int
    data: str
    lode: bool

    def __str__(self): #posso riusare i metodi definiti prima se voglio migliorare; la dataclass è molto utile perchè velocizza
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    #def __eq__(self, other): #non è molto versatile
        #return(self.punteggio == other.punteggio and self.materia == other.materia and self.lode == other.lode)

    def copy(self): #crea una nuova instanza che ha gli stessi parametri dell'instanza di partenza
        return Voto(self.materia, self.punteggio, self.data, self.lode)

    def __hash__(self): #funzione che associa un numero univoco
        #return hash((self.materia, self.punteggio, self.lode))
        return hash(self.materia)

    def __eq__(self, other):
        return self.materia == other.materia
