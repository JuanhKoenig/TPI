
lista = [
    {"nombre": "Valentina", "edad": 23},
    {"nombre": "Martín", "edad": 41},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Sofía", "edad": 19},
    {"nombre": "Carlos", "edad": 32},
    {"nombre": "Tomás", "edad": 30},
    {"nombre": "Diego", "edad": 35},
    {"nombre": "Lucía", "edad": 28}
]


for iteracion in range (len(lista)):
    for persona in range (len(lista)):
        if lista[iteracion]["nombre"] < lista[persona]["nombre"]:
            # p = lista.index(persona)
            lista[iteracion], lista[persona] = lista[persona], lista[iteracion]






for nombre in lista:
    print(nombre)