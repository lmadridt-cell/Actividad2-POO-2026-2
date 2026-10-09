class persona:
  
    def __init__(self, nombre, apellido, numeroDocumentoIdentidad, FechaDeNacimiento, Paisdenacimiento, genero):
  
      self.nombre = nombre
      self.apellido = apellido
      self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
      self.FechaDeNacimiento = FechaDeNacimiento
      self.Paisdenacimiento = Paisdenacimiento
      self.genero = genero


    def imprimir(self):
      print("nombre =",self.nombre)
      print("apellido =",self.apellido)
      print("numeroDocumentoIdentidad =",self.numeroDocumentoIdentidad)
      print("FechaDeNacimiento =",self.FechaDeNacimiento)
      print("Paisdenacimiento =",self.Paisdenacimiento)
      print("genero =",self.genero)

p1= persona("Pedro", "Perez","1053121010", 1998, "Colombia", "H")
p2= persona("Luis", "Leon", "1053223344", 2001,"Colombia", "H")



p1.imprimir()
p2.imprimir()  