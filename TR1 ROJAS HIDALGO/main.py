from  boleta import *
from trabajador import *

boleta1= Boleta("Jhair", "A", 14, 1)
trabajador1= Trabajador(Nombre=input,Sueldos=input, HorasEx=input, MinutosTarde=input)

trabajador1.Inicios()
print("--------------------------")
trabajador1.DatosEntrada()
print("--------------------------")
boleta1.DatosSalida()
