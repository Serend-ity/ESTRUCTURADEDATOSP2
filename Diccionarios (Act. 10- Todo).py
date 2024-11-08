class dicc:
    def __init__(self):
        self.diccionario={}
    def agregar(self, x, y):
        self.diccionario[x] = y
    def modificar(self, x,y):
        self.diccionario[x] = y
    def eliminar(self,x):
        self.diccionario.pop(x,None )
    def mostrar(self):
        print(self.diccionario)

if __name__=="__main__":
       dicc=dicc()

salir= False

while not salir:
    print("\nEliga una opción: \n"
          "1.-Agregar elemento. \n"
          "2.-Modificar elemento.\n"
          "3.-Eliminar elemento.  \n"
          "4.-Mostrar elementos. \n"
          "5.-Salir.  \n")
    opcion = input("¿Qué deseas hacer? : ")
    match opcion:
        case "1":
            cantidad = int(input("Ingresa la cantidad de claves: "))
            for i in range(cantidad):
                clave = input("Introduce la clave: ")
                valor = int(input("Introduce el valor: "))
                dicc.agregar(clave,valor)

        case "2":
            clave = input("Ingrese la clave: ")
            valor = (int(input("Ingresa el nuevo valor: ")))
            dicc.modificar(clave,valor)
        case "3":
            clave = input("Ingrese la clave: ")
            dicc.eliminar(clave)
        case "4":
            dicc.mostrar()
        case "5":
            salir= True