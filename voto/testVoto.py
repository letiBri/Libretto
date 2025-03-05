from voto import Voto, Libretto
# modo per testare il modulo in mood più pulito, posso farlo creando un nuovo file oppure lo faccio all'interno del modulo

v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
v2 = Voto("Pozioni", 30, "2022-02-17", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)

myLib = Libretto(None, [v1, v2])
print(myLib)
myLib.append(v3)
print(myLib)
