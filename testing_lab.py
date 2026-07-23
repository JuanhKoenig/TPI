
ejemplo = ["u", "t", "n"]

for iteracion in ejemplo:
    for letra in ejemplo:
        if letra < iteracion:
            letra, iteracion = iteracion, letra

print(ejemplo)