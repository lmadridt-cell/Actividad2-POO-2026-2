from enum import Enum


class Tip_combustible(Enum):
    gasolina = 0
    bioetanol = 1
    diésel = 2
    biodiésel = 3
    gas_natural = 4


class Tip_automovil(Enum):
    carro_de_ciudad = 0
    subcompacto = 1
    compacto = 2
    familiar = 3
    ejecutivo = 4
    SUV = 5


class Color(Enum):
    blanco = 0
    negro = 1
    rojo = 2
    naranja = 3
    amarillo = 4
    verde = 5
    azul = 6
    violeta = 7


class automovil:
    def __init__(self, marca, modelo, motor, Tip_combustible,
                 Tip_automovil, Nu_puertas, Can_asientos,
                 Velocidad_max, color, Veiculo_autom, Velocidad_actual=0):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.Tip_combustible = Tip_combustible
        self.Tip_automovil = Tip_automovil
        self.Nu_puertas = Nu_puertas
        self.Can_asientos = Can_asientos
        self.Velocidad_max = Velocidad_max
        self.color = color
        self.Velocidad_actual = Velocidad_actual
        self.Veiculo_autom = Veiculo_autom
        self.multas = 0

    def getmarca(self):
        return self.marca

    def getmodelo(self):
        return self.modelo

    def getmotor(self):
        return self.motor

    def getTip_combustible(self):
        return self.Tip_combustible

    def getTip_automovil(self):
        return self.Tip_automovil

    def getNu_puertas(self):
        return self.Nu_puertas

    def getCan_asientos(self):
        return self.Can_asientos

    def getVelocidad_max(self):
        return self.Velocidad_max

    def getcolor(self):
        return self.color

    def getVelocidad_actual(self):
        return self.Velocidad_actual

    def getVeiculo_autom(self):
        return self.Veiculo_autom

    def setmarca(self, marca):
        self.marca = marca

    def setmodelo(self, modelo):
        self.modelo = modelo

    def setmotor(self, motor):
        self.motor = motor

    def setTip_combustible(self, Tip_combustible):
        self.Tip_combustible = Tip_combustible

    def setTip_automovil(self, Tip_automovil):
        self.Tip_automovil = Tip_automovil

    def setNu_puertas(self, Nu_puertas):
        self.Nu_puertas = Nu_puertas

    def setCan_asientos(self, Can_asientos):
        self.Can_asientos = Can_asientos

    def setVelocidad_max(self, Velocidad_max):
        self.Velocidad_max = Velocidad_max

    def setcolor(self, color):
        self.color = color

    def setVeiculo_autom(self, Veiculo_autom):
        self.Veiculo_autom = Veiculo_autom

    def setVelocidad_actual(self, Velocidad_actual):
        self.Velocidad_actual = Velocidad_actual

    def acelerar(self, incrementovelocidad):
        if self.Velocidad_actual + incrementovelocidad <= self.Velocidad_max:
            self.Velocidad_actual = self.Velocidad_actual + incrementovelocidad
        else:
            self.multas = self.multas + 1
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil")

    def desacelerar(self, decrementoVelocidad):
        if self.Velocidad_actual - decrementoVelocidad > 0:
            self.Velocidad_actual = self.Velocidad_actual - decrementoVelocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")

    def frenar(self):
        self.Velocidad_actual = 0

    def calcularTiempoLlegada(self, distancia):
        return distancia / self.Velocidad_actual

    def esta_multado(self):
        if self.multas > 0:
            return "si"
        else:
            return "no"

    def cantidad_multas(self):
        return self.multas

    def imprimir(self):
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor)
        print("Tipo de combustible =", self.Tip_combustible.name)
        print("Tipo de automóvil =", self.Tip_automovil.name)
        print("Número de puertas =", self.Nu_puertas)
        print("Cantidad de asientos =", self.Can_asientos)
        print("Velocidad máxima =", self.Velocidad_max)
        print("Color =", self.color.name)
        print("¿El vehículo es automático? =", self.Veiculo_autom)
        print("Velocidad actual =", self.Velocidad_actual)


auto1 = automovil(
    "Ford",
    2018,
    3,
    Tip_combustible.diésel,
    Tip_automovil.ejecutivo,
    5,
    6,
    250,
    Color.negro,
    "si"
)

auto1.imprimir()

auto1.setVelocidad_actual(100)
print("Velocidad actual =", auto1.getVelocidad_actual())

auto1.acelerar(20)
print("Velocidad actual =", auto1.getVelocidad_actual())

auto1.desacelerar(50)
print("Velocidad actual =", auto1.getVelocidad_actual())

auto1.frenar()
print("Velocidad actual =", auto1.getVelocidad_actual())

auto1.desacelerar(20)

print("¿Está multado?", auto1.esta_multado())
print("Cantidad de multas =", auto1.cantidad_multas())