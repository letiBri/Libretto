from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student("Harry", "Potter", 11, "castani", "azzurri", "Grifondoro", "civetta", "Expecto patronum")
myLib = Libretto(Harry, [])

v1 = Voto("Difesa contro le ari oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 21, "2022-02-12", False)
myLib.append(v1)
myLib.append(v2)

#per fare più veloce posso non salvare nelle variabili
myLib.append(Voto("Trasfigurazione", 21, "2022-06-14", False))
print(myLib.calcolaMedia())

votiFiltrati = myLib.getVotiByPunti(21, False)
print(votiFiltrati)

votoTrasfigurazione = myLib.getVotoByName("Trasfigurazione")
if votoTrasfigurazione is None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione)

print("verifico metodo hasVoto")
print(myLib.hasVoto(v1)) #restituisce True
print(myLib.hasVoto(Voto("Aritmanzia", 30, "2023-07-10", False))) #ritorna False
print(myLib.hasVoto(Voto("Difesa contro le ari oscure", 25, "2022-01-30", False))) #restituisce True, è un'istanza diversa rispetto a v1 ma il metodo verifica i campi

print("verifico metodo hasConflitto")
print(myLib.hasConflitto(Voto("Difesa contro le ari oscure", 21, "2022-01-30", False))) # restituisce True

print("test append modificata")
myLib.append(Voto("Aritmanzia", 30, "2023-07-10", False)) #funziona
#myLib.append(Voto("Difesa contro le ari oscure", 21, "2022-01-30", False)) #scatena errore

myLib.append(Voto("Divinazione", 27, "2021-02-08", False))
myLib.append(Voto("Cura delle creature magiche", 26, "2021-06-14", False))

print("-------------------------------------------------------------------------")
print("Libretto originario")
print(myLib)

nuovoLib = myLib.creaMigliorato()
print("Nuovo Libretto migliorato")
print(nuovoLib) #in questo modo i due libretti sono indipendneti e stampano il voto migliorato
