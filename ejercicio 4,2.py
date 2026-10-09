

import math


class circulo:

    def __init__(self, radio):
        self.radio = radio

    def cal_areaC(self):
        return math.pi * math.pow(self.radio, 2)

    def cal_perimetroC(self):
        return 2 * self.radio * math.pi


class rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def cal_areaR(self):
        return self.base * self.altura

    def cal_perimetroR(self):
        return (2 * self.base) + (2 * self.altura)


class cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def cal_areaCU(self):
        return math.pow(self.lado, 2)

    def cal_perimetroCU(self):
        return 4 * self.lado


class Tri_rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def cal_areaTri_rectangulo(self):
        return (self.base * self.altura) / 2

    def cal_perimetroTri_rectangulo(self):
        return self.base + self.altura + self.cal_hipotenusa()

    def cal_hipotenusa(self):
        return math.pow(
            self.base * self.base + self.altura * self.altura,
            0.5
        )

    def tipo_triangulo(self):
        hipotenusa = self.cal_hipotenusa()

        if (self.base == self.altura) and (self.base == hipotenusa):
            print("Es un triángulo equilátero")

        elif ((self.base != self.altura) and (self.base != hipotenusa)) and (self.altura != hipotenusa):
            print("Es un triángulo escaleno")

        else:
            print("Es un triángulo isósceles")


class rombo:

    def __init__(self, diag_mayor=None, diagonal_menor=None, angulo=None, lado=None):

        self.diag_mayor = diag_mayor
        self.diagonal_menor = diagonal_menor
        self.angulo = angulo
        self.lado = lado

    def area_rom(self):

        if (self.diag_mayor is not None) and \
           (self.diagonal_menor is not None):

            return (self.diag_mayor * self.diagonal_menor) / 2

        elif (self.angulo is not None) and (self.lado is not None):

            diagonal_menor = 2 * self.lado * math.sin(
                math.radians(self.angulo) / 2
            )

            diagonal_mayor = 2 * self.lado * math.cos(
                math.radians(self.angulo) / 2
            )

            return (diagonal_mayor * diagonal_menor) / 2

    def perimetro_rom(self):

        if self.lado is not None:

            return 4 * self.lado

        elif (self.diag_mayor is not None) and \
             (self.diagonal_menor is not None):

            lado = math.pow(
                (self.diag_mayor / 2) ** 2 +
                (self.diagonal_menor / 2) ** 2,
                0.5
            )

            return 4 * lado


class trapecio:

    def __init__(self, base_menor, base_mayor, altura, lado):

        self.base_menor = base_menor
        self.base_mayor = base_mayor
        self.altura = altura
        self.lado = lado

    def cal_area_tra(self):
        return (self.base_menor + self.base_mayor) * self.altura / 2

    def perimetro_tra(self):
        return self.base_menor + self.base_mayor + 2 * self.lado

class PruebaFiguras:
        figura1 = circulo(2) 
        figura2 = rectangulo (1,2)
        figura3 = cuadrado(3)
        figura4 = Tri_rectangulo(3, 5)
        figura5 = rombo (6, 4)
        figura6 = trapecio(4, 8, 3, 5)

        print("El area del circulo =" + figura1.cal_areaC())  
        print("El perimetro del circulo =" + figura1.cal_perimetroC())

        print("El area del rectangulo =" + figura2.cal_areaR())
        print("El perimetro del rectangulo =" + figura2.cal_perimetroR())

        print("El area del cuadrado =" + figura3.cal_areaCU())
        print("El perimetro del cuadrado =" + figura3.cal_perimetroCU())

        print("El area del triangulo rectangulo =" + figura4.cal_areaTri_rectangulo())
        print("El perimetro del triangulo rectangulo =" + figura4.cal_perimetroTri_rectangulo())

        print("El area del rumbo rectangulo =" + figura5.area_rom())
        print("El perimetro del rumbo rectangulo =" + figura5.perimetro_rom())

        print("El area del trapecio =" + figura6.cal_area_tra())
        print("El perimetro del trapecio =" + figura6.perimetro_tra())