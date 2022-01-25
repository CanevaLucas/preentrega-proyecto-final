class  Persona():

    tipo_de_usuario = "cliente"

    def __init__(self, nombre, apellido, edad, mail):

        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.mail = mail

    def comprador(self):
        print("comprador")

persona1 = Persona("Lucas", "Caneva", 22, "lucasncaneva@gmail.com")
persona2 = Persona("Gabriel", "Caneva", 52, "gab@gmail.com")

print(f"mi nombre es: {persona1.nombre}")
print(persona2.nombre)
print(persona1.tipo_de_usuario)

print(Persona.tipo_de_usuario)
