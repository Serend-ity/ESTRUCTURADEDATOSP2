class platos:
    def __init__(self):
        self.Persona1 = set()
        self.Persona2 = set()

    def agregar(self, a, c):
        if c == 1:
            self.Persona1.add(a)
        else:
            self.Persona2.add(a)

    def mostrar_todos(self):
        if len(self.Persona1 and self.Persona2) == 0:
            print("No hay elementos. ")
        if len(self.Persona1 & self.Persona2) ==0:
            print("No hay elementos en común. ")
        else:
            print(f"Los platos en común son: {self.Persona1 & self.Persona2}")

    def mostrar_prg(self):
        if len(self.Persona1 and self.Persona2) == 0:
            print("No hay elementos. ")
        else:
            print(self.Persona1)
            print(self.Persona2)


if __name__ == "__main__":
    platos = platos()

salir = False
while not salir:
    print("\nEliga una opción: \n"
          "1.-Agregar un plato favorito de Persona 1. \n"
          "2.-Agregar un plato favorito de Persona 2. \n"
          "3.-Mostrar los platos en comun platos.\n"
          "4.-Mostrar todos los platos. \n"
          "6.-Salir. \n")
    opcion = input("¿Qué deseas hacer? : ")
    match opcion:
        case "1":
            plato = input("Agrega un plato: ")
            x = 1
            platos.agregar(plato, x)

        case "2":
            plato = input("Agrega un elemento: ")
            x = 0
            platos.agregar(plato, x)
        case "3":
            platos.mostrar_todos()
        case "4":
            platos.mostrar_prg()
        case "5":
            salir = True