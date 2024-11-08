
class cursos:
    def __init__(self):
        self.Programacion= set()
        self.Redes= set()

    def agregar(self, a,c):
        if c==1:
            self.Programacion.add(a)
        else:
            self.Redes.add(a)
    def mostrar_todos(self):
        if len(self.Programacion and self.Redes)==0:
            print("No hay elementos. ")
        else:
            print(self.Programacion|self.Redes)
    def mostrar_prg(self):
        if len(self.Programacion)==0:
            print("No hay elementos. ")
        else:
            print(self.Programacion)

    def mostrar_red(self):
        if len(self.Redes)==0:
            print("No hay elementos. ")
        else:
            print(self.Redes)


if __name__=="__main__":
    cursos=cursos()
    
salir= False
while not salir:
    print("\nEliga una opción: \n"
          "1.-Agregar un alumno a Programacion. \n"
          "2.-Agregar un alumno a Redes. \n"
          "3.-Mostrar los alumnos en ambos cursos.\n"
          "4.-Mostrar los alumnos en Programacion.\n"
          "5.-Mostrar los alumnos en Redes.\n"
          "6.-Salir. \n")
    opcion = input("¿Qué deseas hacer? : ")
    match opcion:
        case "1":
            alumno=input("Agrega un elemento: ")
            x=1
            cursos.agregar(alumno,x)

        case "2":
            alumno=input("Agrega un elemento: ")
            x=0
            cursos.agregar(alumno,x)
        case "3":
            cursos.mostrar_prg()
        case "4":
            cursos.mostrar_todos()
        case "5":
            cursos.mostrar_todos()
        case "6":
            salir= True