class stack:
    def __init__(self):
        self.pila=[]
        for i in range(11):
            self.pila.append(i+1)
#Verifica que la lista esta vacia.
    def  esta_vacia(self):
        return len(self.pila) == 0
#Metodo push.
    def agregar_elemento(self, elemento):
        self.pila.append(elemento)
#Elementos de la lista.
    def elementos(self):
        for i in self.pila:
            print(i)
#Metodo pop.
    def sacar_elemento(self):
        self.pila.pop(len(self.pila)-1)


if __name__=="__main__":
    stack = stack()

if stack.esta_vacia():
    print("La lista esta vacia.")

salir= False
while not salir:
    print("\nEliga una opción: \n"
          "1.-Agregar un elemento. \n"
          "2.-Eliminar el ultimo elemento.\n"
          "3.-Revisar los elementos. \n"
          "4.-Salir. \n")
    opcion = input("¿Qué deseas hacer? : ")
    match opcion:
        case "1":
            elemento=(int(input("Agrega un elemento: ")))
            stack.agregar_elemento(elemento)
            stack.elementos()
        case "2":
            stack.sacar_elemento()
            stack.elementos()
        case "3":
            stack.elementos()
        case "4":
            salir= True