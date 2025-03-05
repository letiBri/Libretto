from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student("Harry", "Potter", 11, "castani", "azzurri", "Grifondoro", "civetta", "Expecto patronum")
myLib = Libretto(Harry, [])

v1 = Voto("Difesa contro le ari oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 21, "2022-02-12", False)
myLib.append(v1)
myLib.append(v2)

#per fare più veloce
myLib.append(Voto("Trasfigurazione", 21, "2022-06-14", False))
myLib.calcolaMedia()

votiFiltrati = myLib.getVotiByPunti(21, False)
print(votiFiltrati)

votoTrasfigurazione = myLib.getVotoByName("Trasfigurazione")
if votoTrasfigurazione is None:
    print("Voto non trovato")
else:
    print(votoTrasfigurazione)
