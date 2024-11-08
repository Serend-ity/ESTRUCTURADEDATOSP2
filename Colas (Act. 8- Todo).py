class queue:
    def __init__(self):
        self.pila= []
        for i in range(10):
            self.pila.append(i+1)
#Metodo front, primer elemento.
    def front(self):
        if len(queue.pila)==0:
            print("No hay elementos en la lista. ")
        else:
            print(self.pila[0])
#Metodo back, ultimo elemento.
    def back(self):
        if len(queue.pila)==0:
            print("No hay elementos en la lista. ")
        else:
            print(self.pila[len(self.pila)-1],end=" ")
#Metodo pop, eliminar todos los elementos. (FIFO)
    def pop(self):
        for x in range(len(self.pila)):
            self.pila.pop(0)
            print(x,end=" ")
#Metodo push, agrega elemento a la cola.
    def push(self, element):
        self.pila.append(element)
#Imprime los elementos de cada posición.
    def elementos(self):
        for c in range(len(self.pila)):
            print(self.pila[c],end=" ")

if __name__=="__main__":
    queue = queue()

salir= False
while not salir:
    print("\nEliga una opción: \n"
          "1.-Primer elemento. \n"
          "2.-Ultimo elemento.\n"
          "3.-Agregar elemento. \n"
          "4.-Eliminar elementos. \n"
          "5.-Revisar elementos "
          "6.-Salir. ")
    opcion = input("¿Qué deseas hacer? : ")
    match opcion:
        case "1":
            queue.front()
        case "2":
            queue.back()
        case "3":
            elemento = (int(input("Agrega un elemento: ")))
            queue.push(elemento)
        case "4":
            queue.pop()
        case "5":
            queue.elementos()
        case "6":
            salir= True