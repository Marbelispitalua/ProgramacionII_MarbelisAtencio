perro = {}

perro["Nombre"] = "Soky"
perro["Color"] = "Cafe"
perro["Raza"] = "Pastor_Aleman"
perro["Edad"] = "1"

estudiante = {
    
     "nombre" : "Marbelis",
     "apellido" : "Atencio",
     "sexo" : "Femenino",
     "edad" : "18",
     "estado civil" : "Soltero",
     "habilidades" : ['lectura','Aprende_rapido','eficacia','paciencia'],
     "país" : "Colombia",
     "ciudad" : "cartagena",
     "dirección" : "Barrio_boston"
 }

print(len(estudiante))

print(estudiante["habilidades"])

print(type(estudiante["habilidades"]))

estudiante["habilidades"] = ['lectura','Aprende_rapido','eficacia','paciencia','comunicacion']

claves = estudiante.keys()

valores = estudiante.values()

print(claves)
print(valores)

print(estudiante.items())

estudiante.popitem()

del perro