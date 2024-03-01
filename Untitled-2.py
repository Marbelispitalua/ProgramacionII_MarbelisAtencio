class Lote: 
    
    def __init__(self,Largo, Ancho, Constructora): 
        
        self.Largo= Largo
        self.Ancho= Ancho
        self.constructora = Constructora
        
        def calcular_area(self):
            
            print(self.Largo * self.Ancho)
            
    def printcontructora(self):
        
        print(self.constructora)
        
        
class casa(Lote):  
    def __init__(self, Largo, Ancho, Constructora, Propietario, Telefono):
        
        super().__init__(Largo,Ancho,Constructora)
        self.Propietario= Propietario
        self.Telefono= Telefono
        
    def printpropietario(self):
        print(self.Propietario)
        
    def printTelefono(self):
        print(self.Telefono)
        
    c= Casa (50000,25000,"Lambana", "Marbelis", "3223474678") 
    
    c.printpropietario()
    c.Calcular_area()
    c.printTelefono()
    c.printcontructora()

    