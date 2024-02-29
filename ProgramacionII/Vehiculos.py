class vehiculo:
    
    def __init__(self,marca,modelo,velocidad_maxima,caballos_de_fuerza,traccion):
        
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.caballos_de_fuerza = caballos_de_fuerza
        self.traccion = traccion
        
V = vehiculo ("Nissan ","GT-R Skyline","315 Kmh","276hp","traccion en las cuatro ruedas")

print(" la marca del auto es: "+V.marca +"\n el modelo del deportivo es el: "+V.modelo+"\n la velocidad maxima del auto es de: "+V.velocidad_maxima+"\n la cantidad de caballos de fuerza es de: "+V.caballos_de_fuerza+"\n la traccion del auto es : "+V.traccion)

        

    