lista=[]

for i in range(5):
        print("Ingresa los valores: ")
        lista.extend(input())
print(lista)

contador=0
numero_mas_repetido= 0
repeticiones=0
for num in lista:
    contador=lista.count(num)
    if contador>repeticiones:
        repeticiones=contador
        numero_mas_repetido=num

print(numero_mas_repetido)
print(repeticiones)

for num in lista:
    if num==numero_mas_repetido:
        lista.remove(num)

print(lista)