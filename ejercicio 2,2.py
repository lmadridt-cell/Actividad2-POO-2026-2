
from enum import Enum

class Tipoplaneta(Enum):
    GASEOSO = 0
    TERRESTRE = 1
    ENANO = 2


class planeta:
    def __init__(self, nombre = None, cantsatelites = 0, masa = 0, volumen = 0,
                 diametro = 0, Distsol = 0, Tipoplaneta = None, odservable = False,
                 per_orbital = 0, per_rotación = 0):

        self.nombre = nombre
        self.cantsatelites = cantsatelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.Distsol = Distsol
        self.Tipoplaneta = Tipoplaneta
        self.odservable = odservable
        self.per_orbital = per_orbital
        self.per_rotación = per_rotación

    def imprimir(self):
        print("nombre =", self.nombre)
        print("cantsatelites =", self.cantsatelites)
        print("masa =", self.masa)
        print("volumen =", self.volumen)
        print("diametro =", self.diametro)
        print("Distsol =", self.Distsol)
        print("Tipo planeta =", self.Tipoplaneta.name)
        print("odservable =", self.odservable)
        print("per_orbital =", self.per_orbital)
        print("per_rotación =", self.per_rotación)

    def calcular_densidad(self):
        return self.masa / self.volumen

    def planeta_exterior(self):
        limite = 149597870 * 3.4

        if self.Distsol > limite:
            return True
        else:
            return False


p1 = planeta(
    "Tierra", 1, 5.9736E24, 1.08321E12, 12742,
    150000000, Tipoplaneta.TERRESTRE, True
)

p1.imprimir()
print("Densidad =", p1.calcular_densidad())
print("¿Es planeta exterior?", p1.planeta_exterior())
print()


p2 = planeta(
    "Júpiter", 79, 1.899E27, 1.4313E15, 139820,
    750000000, Tipoplaneta.GASEOSO, True
)

p2.imprimir()
print("Densidad =", p2.calcular_densidad())
print("¿Es planeta exterior?", p2.planeta_exterior())
print()