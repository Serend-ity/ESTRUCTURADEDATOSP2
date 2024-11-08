
lista=[]
i = 0
j = input("Ingresa los valores: ")
lista.extend(j.split(","))
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