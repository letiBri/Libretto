class Person:
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self._cognome = cognome  #per definire un attributo privato
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.__prova = None
        self.incantesimo = incantesimo

    def __str__(self):
        return f"Person: {self.nome} {self.cognome}\n"

    @property  #li usaimo raramente perchè essendo variabili pubbliche accediamo direttamente
    def cognome(self):
        return self._cognome  #equivalente al getter si java

    @cognome.setter
    def cognome(self, value):
        #controlli per verificare che value sia compatibile con cognome
        self._cognome = value  #equivalente del setter


class Student(Person):  #ereditarietà, quindi prende tutti i metodi di Person
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, animale, incantesimo="Non ancora definito"):
        # se passo **kwargs passa un numero arbitrario di argomenti e li inserisce in una mappa
        # se passo *args passa un numero arbitrario di argomenti e li inserisce in una lista
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.animale = animale
    def copy(self):
        return Student(self.nome, self.cognome, self.eta, self.capelli, self.occhi, self.casa, self.animale, self.incantesimo)

    def __str__(self):
        return f"Student: {self.nome} - {self.cognome} - {self.casa}\n "

    def __repr__(self):
        return f"Student(nome, cognome, eta, capelli, occhi, casa, animale)"

    def prettyPrint(self):
        print("Voglio stampare meglio")


class Teacher(Person):
    def __init__(self, nome, cognome, eta,
                 capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia

    def __str__(self):
        return f"Teacher: {self.nome} - {self.cognome} - {self.materia}\n "


class Casa:
    def __init__(self, nome, studenti=[]):
        self.nome = nome
        self.studenti = studenti

    def addStudente(self, studente):
        self.studenti.append(studente)  # --> [ x,x,x [s1, s2]]
        #self.studenti.extend(studente) # --> [ x,x,x, s1, s2 ]

    def __str__(self):
        if len(self.studenti) == 0:
            return f"La casa {self.nome} + è vuota."
        mystr = f"\n Lista degli studenti iscritti alla casa {self.nome}\n"
        for s in self.studenti:
            mystr += str(s)
        return mystr

class Scuola:
    def __init__(self, case):
        self.case = case
    def __str__(self):
        mystr = ""
        for c in self.case:
            mystr += str(c) #delegation al metodo __str__  in Casa
        return mystr
