
lista = [6, 3, 8, 5, 1, 4, 2, 9, 0, 7]


for iteracion in range(len(lista)):
    for numero in lista:
        if lista[iteracion] < numero:
            p = lista.index(numero)
            lista[iteracion], lista[p] = lista[p] , lista[iteracion]

print(lista)

