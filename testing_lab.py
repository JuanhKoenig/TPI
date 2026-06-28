lista = [
    {"nombre": "Lala", "edad": 30},
    {"nombre": "Juan", "edad": 28},
    {"nombre": "Pedro", "edad": 29},
    {"nombre": "Sofía", "edad": 22},
    {"nombre": "Lolo", "edad": 31},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "María", "edad": 27}
]


testing = lista[-1]["edad"]
menor = lista[0]
for item in range(1, len(lista)):

    anterior = lista[item - 1]
    anterior_edad = anterior["edad"]
    
    actual = lista[item]
    actual_edad = actual["edad"]

    if actual["edad"] < menor["edad"]:
        menor = actual
    
print(f"el menor es {menor["nombre"]} con {menor["edad"]} años")