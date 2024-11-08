compras=["Manzana","Pera","Arroz"]

print(compras)
def a1():
    compras.append(input())
    print(compras)
def a2():
    print(compras)

    delete= int(input("¿Qué elementos deseas eliminar?"))
    compras.pop(delete)
    print(compras)
change= 1
while change != 4:
    print('1.Agregar elemento.\n2.Quitar elemento')
    change = int(input('elige una opcion: '))
    if change == 1:
        a1()
    elif change == 2:
        a2()
        print('exit...')
