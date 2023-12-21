class Persona():
    def __init__(self, rut, nombre, region, peticion):
        self.rut = rut
        self.nombre = nombre
        self.region = region
        self.peticion = peticion

    def mostrar_datos(self):
        print("RUT: ", self.rut)
        print("Nombre: ", self.nombre)
        print("Región: ", self.region)
        print("Petición de Ayuda: ", self.peticion)

    def getRut(self):
        return self.rut

class Vuelo():
    def __init__(self, origen, destino, hora_salida):
        self.pasajeros = []
        self.origen = origen
        self.destino = destino
        self.hora_salida = hora_salida

    def buscarPasajero(self, rut):
        for persona in self.pasajeros:
            if rut == persona.getRut():
                return True
        return False

    def agregar_pasajero(self, Persona):
        if not self.buscarPasajero(Persona.getRut()):
            self.pasajeros.append(Persona)
            print("Pasajero agregado con éxito")
        else:
            print("Esta persona ya se encuentra en el avión")

    def eliminar_Pasajero(self, Persona):
        for persona in self.pasajeros:
            if persona.getRut() == Persona.getRut():
                self.pasajeros.remove(persona)
                print("Se ha eliminado al pasajero correctamente")
                return
        print("El pasajero no existe en este vuelo")

    def modificar_pasajero(self, Persona):
        for persona in self.pasajeros:
            if persona.getRut() == Persona.getRut():
                indice = self.pasajeros.index(persona)
                self.pasajeros[indice] = Persona
                print("Información del pasajero actualizada exitosamente.")

    def listar_pasajeros(self):
        for i in range(len(self.pasajeros)):
            print("\n\nDatos del Pasajero N°", i + 1)
            self.pasajeros[i].mostrar_datos()

                
persona1 = Persona('17256349-8', 'Andrés', 'Santiago', "Ayuda para comprar comestibles")
persona2 = Persona('10256349-1', 'María', 'Concepción', "Ayuda para ir al supermercado")
vuelo1 = Vuelo('Santiago', 'Valparaíso', '10:00')
vuelo1.agregar_pasajero(persona1)
vuelo1.agregar_pasajero(persona2)

while True:
    print("\nMenu Principal")
    print("1. Agregar Pasajero")
    print("2. Eliminar Pasajero")
    print("3. Modificar Información de un Pasajero")
    print("4. Listar Pasajeros")
    print("5. Salir")
    opcion = input("Ingrese una Opción: ")
    if opcion == "1":
        persona3 = Persona(input("Ingrese RUT del nuevo pasajero: "),
                           input("Nombre: "),
                           input("Apellido: "),
                           input("Motivo del viaje: "))
        vuelo1.agregar_pasajero(persona3)
    elif opcion == "2":
        if len(vuelo1.pasajeros)== 0:
            print("No hay pasajeros en este vuelo")
        else:
            rut = input("Ingrese el RUT del pasajero a eliminar: ")
            vuelo1.eliminar_Pasajero(Persona(rut,"","",""))
    elif opcion == "3":
        if len(vuelo1.pasajeros) > 0:
            rut = input("Ingrese el rut a modificar: ")
            if vuelo1.buscarPasajero(rut):
                persona3 = Persona(rut,
                           input("Nombre: "),
                           input("Apellido: "),
                           input("Motivo del viaje: "))
                vuelo1.modificar_pasajero(persona3)
            else:
                print("Este RUT no corresponde a ningún pasajero en este vuelo")
    elif opcion == "4":
        vuelo1.listar_pasajeros()
    else:
        print("Adios.")

