class Boleta():
    def __init__(self, Nombre, Category, HorasExtra,Tardanzas):
         self.Nombre=Nombre
         self.Category=Category
         self.HorasExtra=HorasExtra
         self.Tardanzas=Tardanzas
    
    def Categoria(self):
        if self.Category.lower() == "a":
            Sueldosb=3000
            return Sueldosb
            
        elif self.Category.lower() == "b":
            Sueldosb=2500 
            return Sueldosb
            
        elif self.Category.lower() == "c":
            Sueldosb=2000
            return Sueldosb
            
        else:
            print("La categoria ingresada es incorrecta, pruebe de nuevo.")
            
    def Hours (self):
        HorasExtra= (self.Categoria()/24)*self.Tardanzas
        return round((HorasExtra),2)
    def Tarde(self):
        Tardanzas= ((self.Categoria()/24)/60)*self.HorasExtra
        return round((Tardanzas),2)
    def netamente(self):
        SueldoNeto= (self.Categoria()- self.Tardanzas + self.HorasExtra)
        return ((SueldoNeto),2)
    
    def DatosSalida(self):
        print(" ")
        print("******BOLETA DE PAGO******")
        print("Nombre:               ", self.Nombre)
        print("Categoria:            ", self.Category)
        print("Sueldo Basico:        ", self.Categoria())
        print("Horas Extra:          ", self.Hours())
        print("Tardanzas(minutos):   ", self.Tarde())
        print("Sueldo Neto:          ", self.netamente())
        