class Persona:

    def __init__(self, nombre, apellido, cedula, correo, telefono):

            self.nombre = nombre
            self.apellido = apellido
            self.cedula = cedula
            self.correo = correo
            self.telefono = telefono

    
P= Persona("Marbelis","Atencio"," 1063145199","matenciopitalua2005@gmail.com"," 3223474678")

print(" mi nombre es: "+P.nombre,"\n mi apellido es: "+P.apellido,"\n mi cedula es: "+P.cedula,"\n mi correo es: "+P.correo,"\n mi numero de telefono: "+P.telefono)

