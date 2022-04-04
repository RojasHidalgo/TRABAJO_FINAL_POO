#crear una clase donde se delcare los datos de los trabajadores
class Trabajador:

    def __init__(self, Nombre, Sueldos, HorasEx, MinutosTarde):
        self.Nombre =Nombre
        self.Sueldos = Sueldos
        self.HorasEx = HorasEx
        self.MinutosTarde= MinutosTarde
        
    def Inicios(self):
        self.Nombre =input("Ingresar el nombre del trabajador: ")
        self.Sueldos = input("Ingresar la categoria que pertenece (a/b/c): ")
        self.HorasEx = int(input("Ingresar las horas extras realizadas: "))
        self.MinutosTarde = int(input("Ingresar las tardanzas(minutos): "))
        
    def DatosEntrada(self):
        print(" ")
        print(" ")
        print("*****DATOS DE ENTRADA*****")
        print("TRABAJADOR:     ", self.Nombre)
        print("CATEGORIA:      ", self.Sueldos)
        print("HORAS EXTRA:    ", self.HorasEx)
        print("TARDANZA:       ", self.MinutosTarde)

# trabajador1=Trabajador()
# trabajador1.DatosEntrada()

