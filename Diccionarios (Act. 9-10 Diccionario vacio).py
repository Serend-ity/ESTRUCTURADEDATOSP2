mi_diccionario = {}

# Definir la cantidad de elementos que quieres agregar
num_elementos = int(input("¿Cuántas claves y valores deseas ingresar? "))

for _ in range(num_elementos):
    clave = input("Introduce la clave: ")
    valor = input("Introduce el valor: ")
    mi_diccionario[clave] = valor

print("Diccionario final:", mi_diccionario)