#Leer el CSV y cargarlo en una lista de diccionarios

import csv

#paises.csv
# nombre,poblacion,superficie,continente
# Argentina,45376763,2780400,América
# Brasil,213993437,8515767,América
# Chile,19116201,756102,América
# Colombia,51265844,1141748,América
# México,126705138,1964375,América
# Japón,125800000,377975,Asia
# China,1412600000,9596960,Asia
# India,1380004385,3287263,Asia
# Corea del Sur,51780579,100210,Asia
# Indonesia,273523621,1904569,Asia
# Alemania,83149300,357022,Europa
# Francia,67391582,551695,Europa
# España,47351567,505990,Europa
# Italia,60367477,301340,Europa
# Reino Unido,67886011,243610,Europa
# Nigeria,206139589,923768,África
# Etiopía,114963588,1104300,África
# Egipto,102334404,1001449,África
# Sudáfrica,59308690,1219090,África
# Kenya,53771296,580367,África
# Australia,25499884,7692024,Oceanía
# Nueva Zelanda,5084300,270467,Oceanía



paises = []

with open("paises.csv", "r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo) 
    for linea in lector:
        paises.append({"nombre" : linea["nombre"], "poblacion" : int(linea["poblacion"]), "superficie": int(linea["superficie"]), "continente" : linea["continente"]})



#MENU

def menu_principal():

    while True:
        try:
            # eleccion = int(input("1)Ver Datos\n2)Agregar país\n3)Actualizar datos\n4)Buscar pais\n5)Estadisticas\n6)Salir\n"))
            eleccion = int(input(
                "1)Ver Datos\n"
                "2)Agregar país\n"
                "3)Actualizar datos\n"
                "4)Buscar\n"
                "5)Estadisticas\n"
                "6)Ordenar\n"
                "7)Salir\n"
            ))
            if eleccion not in (1, 2, 3, 4, 5, 6, 7):
                raise ValueError("fuera de rango")
            
        except ValueError as e:
            if str(e) == "fuera de rango":
                print("\nOpcion fuera de rango\n")
            else:
                print("\nError, use solo numeros\n")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
        
        else:
            return eleccion




#VER DATOS:

def ver_datos():

    for item in paises:
        print(item)
# FILTROS

    while True:
        try:
            datos_eleccion = int(input(
                "1)Filtrar por continente\n"
                "2)Filtrar por rango de poblacion\n"
                "3)Filtrar por rango de superficie\n"
                "4)Volver\n"
            ))
            if datos_eleccion not in (1, 2, 3, 4): #4 es para volver
                raise ValueError("fuera de rango")
        
        except ValueError as e:
            if str(e) == "fuera de rango":
                print("\nOpcion fuera de rango\n")
            else:
                print("\nOpcion invalida, use solo numeros\n")
            
        if datos_eleccion == 1:
            

            try:

                continentes = ["América", "África", "Oceanía", "Europa", "Asia", "Antártida"]

                print("seleccione continente: ")
                for i in range(len(continentes)):
                    index = i + 1
                    print(f"{index}) {continentes[i]}")
                continente_seleccionado = int(input("> "))

                if continente_seleccionado not in (1, 2, 3, 4, 5, 6):
                    raise ValueError("fuera de rango")
            except ValueError as e:
                if str(e) == "fuera de rango":
                    print("\nOpcion fuera de rango\n")
                else:
                    print("\nOpcion invalida, use numeros del 1 la 6\n")
            else:
                for item in paises:
                    if item["continente"] == continentes[continente_seleccionado - 1]: #-1 para que se ajuste al indice de la lista continentes
                        print(item)
            

        
        elif datos_eleccion == 2:
            
            try:

                rango_minimo = int(input("Ingrese el rango minimo: "))
                if rango_minimo < 0:
                    raise ValueError("negativo")

                rango_maximo = int(input("Ingrese el rango maximo: "))
                if rango_maximo < 0:
                    raise ValueError("negativo")
                
                elif rango_maximo < rango_minimo:
                    raise ValueError("no es maximo")

            except ValueError as e:
                if str(e) == "negativo":
                    print("\nNo se permiten valores negativos\n")
                
                elif str(e) == "no es maximo":
                    print("\nEl valor maximo no puede ser menor que el valor minimo\n")
                    
                else:
                    print("\nError, use solo numeros positivos\n")

            
            else:
                for item in paises:
                    if (item["poblacion"] > rango_minimo) and (item["poblacion"] < rango_maximo):
                        print(item)




        elif datos_eleccion == 3:
            #copiar y pegar de la opcion anterior y cambiar poblacion por superficie
            try:

                rango_minimo = int(input("Ingrese el rango minimo: "))
                if rango_minimo < 0:
                    raise ValueError("negativo")

                rango_maximo = int(input("Ingrese el rango maximo: "))
                if rango_maximo < 0:
                    raise ValueError("negativo")
                
                elif rango_maximo < rango_minimo:
                    raise ValueError("no es maximo")

            except ValueError as e:
                if str(e) == "negativo":
                    print("\nNo se permiten valores negativos\n")

                elif str(e) == "no es maximo":
                    print("\nEl valor maximo no puede ser menor que el valor minimo\n")

                else:
                    print("\nError, use solo numeros positivos\n")

            
            else:
                for item in paises:
                    if (item["superficie"] > rango_minimo) and (item["superficie"] < rango_maximo):
                        print(item)
        else:
            break

#AGREGAR PAIS CON VALIDACIONES


def agregar_pais_nombre():    
    while True:
        #nombre del pais
        try: 
            pais_nuevo = input("Nombre del pais: ").strip().title()

            #validar que no este ya en la lista de diccionarios
            for pais in paises:
                if pais_nuevo == pais["nombre"]:
                    raise ValueError("repetido")
                elif pais_nuevo == "":
                    raise ValueError("vacio")
                
        except ValueError as e:
            if str(e) == "repetido":
                print(f"Error, el pais {pais_nuevo} ya esta registrado en la lista\n")

            elif str(e) == "vacio":
                print("No se permiten nombres vacios")

            else:
                print(f"Error inesperado: {e}\n")

        else:
            print(f"nombre del pais registrado exitosamente: {pais_nuevo}\n")
            return pais_nuevo

def agregar_pais_poblacion():
    while True:
        #registrar poblacion
        try: 
            pais_nuevo_poblacion = int(input("Poblacion: "))
            if pais_nuevo_poblacion < 0:
                raise ValueError("negativo")
            
        except ValueError as e:
            if str(e) == "negativo":
                print("Error. El valor de la poblacion no puede ser negativo\n")
            else:
                print("Error. Use numeros para indicar la poblacion\n")

        except Exception as e:
            print(f"Error desconocido: {e}")
        
        else:
            print(f"poblacion registrada exitosamente: {pais_nuevo_poblacion}\n")
            return pais_nuevo_poblacion

def agregar_pais_superficie():
    while True:
        #registrar superficie
        try:
            pais_nuevo_superficie = int(input("Superficie: "))

            if pais_nuevo_superficie < 0:
                raise ValueError("negativo")
            
        except ValueError as e:
            if str(e) == "negativo":
                print("Error, no se permiten numeros negativos para la superficie\n")
            else:
                print("Error. use numeros para indicar la superficie\n")
            
        except Exception as e:
            print(f"Error desconocido: {e}")

        else:
            print(f"Superficie registrada exitosamente: {pais_nuevo_superficie}\n")
            return pais_nuevo_superficie

def agregar_pais_continente():    
    while True:
        #registrar continente
        #para este vamos a usar un menu
        try:
            pais_nuevo_continente = int(input("Continente:\n1. Asia\n2. África\n3. América\n4. Antártida\n5. Europa\n6. Oceanía\n"))
            if pais_nuevo_continente not in (1, 2, 3, 4, 5, 6):
                raise ValueError("fuera de rango")
        
        except ValueError as e:
            if str(e) == "fuera de rango":
                print("opcion fuera de rango")
            else:
                print("Error. por favor, elija una de las opciones con los numeros del 1 al 6: \n")

        else:
            if pais_nuevo_continente == 1:
                pais_nuevo_continente = "Asia"
            
            elif pais_nuevo_continente == 2:
                pais_nuevo_continente = "África"

            elif pais_nuevo_continente == 3:
                pais_nuevo_continente = "América"

            elif pais_nuevo_continente == 4:
                pais_nuevo_continente = "Ántartida"

            elif pais_nuevo_continente == 5:
                pais_nuevo_continente = "Europa"

            else:
                pais_nuevo_continente = "Oceanía"
            print(f"Contiente del pais registrado exitosamente: {pais_nuevo_continente}")
            return pais_nuevo_continente


#ya esta todo registrado y validado, se puede agregar:
def agregar_pais():
    paises.append({
        "nombre": agregar_pais_nombre(),
        "poblacion": agregar_pais_poblacion(),
        "superficie": agregar_pais_superficie(),
        "continente": agregar_pais_continente()
    })


#BUSCAR
# no es una funcion de usuario, esto es una herramienta que complementa a las funciones
# de actualizar datos y buscar 

def buscar():
    while True:    
        try:
            pais_buscado = input("Buscar: ").strip().title()

            pais_encontrado = False

            for pais in paises:
                if pais_buscado.lower() in pais["nombre"].lower():
                    pais_encontrado = True
                    pais_datos = pais
                
                
            if pais_encontrado == False:
                raise ValueError("no encontrado")
            
        except ValueError as e:
            if str(e) == "no encontrado":
                print(f"Pais \"{pais_buscado}\" no encontrado\n")
            else:
                print("Error desconocido")
        
        else:
            return pais_datos
        

#ACTUALIZAR DATOS

def actualizar_datos():

    while True:
        
        print("\nEditando...\n")
        editar_datos = buscar()
        print(editar_datos)

        try:

            tipo_de_dato = int(input("Editar: \n1.Nombre\n2.Poblacion\n3.Superficie\n4.Continente\n"))

            if tipo_de_dato not in (1, 2, 3, 4):
                raise ValueError("fuera de rango")
            
        except ValueError as e:
            if str(e) == "fuera de rango":
                print("\nError. opcion fuera de rango, use los numeros del 1 al 4\n")
            else:
                print("\nError. Use numeros\n")
        
        else:

            if tipo_de_dato == 1:
                editar_datos["nombre"] = agregar_pais_nombre()
                
            elif tipo_de_dato == 2:
                editar_datos["poblacion"] = agregar_pais_poblacion()

            elif tipo_de_dato == 3:
                editar_datos["superficie"] = agregar_pais_superficie()

            else:
                editar_datos["continente"] = agregar_pais_continente()
            
            break


#ESTADISTICAS

def estadisticas_extremos(paises):
    #buscar el menor y el mayor de las poblaciones y superficies

    
    mayor_poblacion = paises[0]
    menor_poblacion = paises[0]

    mayor_superficie = paises[0]
    menor_superficie = paises[0]

    for item in range(1, len(paises)):
        
        indice_actual = paises[item]

        #POBLACION

        if indice_actual["poblacion"] < menor_poblacion["poblacion"]:
            menor_poblacion = indice_actual
        
        if indice_actual["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = indice_actual
            
        #SUPERFICIE

        if indice_actual["superficie"] < menor_superficie["superficie"]:
            menor_superficie = indice_actual

        if indice_actual["superficie"] > mayor_superficie["superficie"]:
            mayor_superficie = indice_actual
    
    return mayor_poblacion, menor_poblacion, mayor_superficie, menor_superficie


def estadisticas_promedio(paises):
    promedio_poblacion = 0
    promedio_superficie = 0

    for item in paises:
        promedio_poblacion += item["poblacion"]
        promedio_superficie += item["superficie"]

    promedio_poblacion = round((promedio_poblacion / len(paises)), 2)
    promedio_superficie = round((promedio_superficie / len(paises) ), 2)

    return promedio_poblacion, promedio_superficie




def ver_estadisticas():
    extremos = estadisticas_extremos(paises) #tupla con 4 diccionarios 
    promedios = estadisticas_promedio(paises) #tupla con 2 diccionarios

    mayor_poblacion = extremos[0]
    menor_poblacion = extremos[1]
    mayor_superficie = extremos[2]
    menor_superficie = extremos[3]

    print("\nESTADISTICAS: \n")

    print("\nPOBLACION: \n")
    print(f"Mayor: {mayor_poblacion["nombre"]} - {mayor_poblacion["poblacion"]} habitantes\n")
    print(f"Menor: {menor_poblacion["nombre"]} - {menor_poblacion["poblacion"]} habitantes\n")
    print(f"Promedio: {promedios[0]}\n")
    print(f"\nSUPERFICIE: \n")
    print(f"Mayor: {mayor_superficie["nombre"]} : {mayor_superficie["superficie"]} Km2\n")
    print(f"Menor: {menor_superficie["nombre"]} : {menor_superficie["superficie"]} Km2\n")
    print(f"Promedio: {promedios[1]} Km2\n")



#ORDENAR

def ordenar():
    
    while True:
        try:

            ordenamiento = int(input(
                "1)Ordenar por nombre\n"
                "2)Ordenar por Poblacion\n"
                "3)Ordenar por superficie\n"
                "4)Volver\n"
            ))

            if ordenamiento not in (1, 2, 3, 4):
                raise ValueError("fuera de rango")

        except ValueError as e:
            if str(e) == "fuera de rango":
                print("\nError, opcion fuera de rango\n")
            else:
                print("\nError, use numeros del 1 al 4 por favor\n")
        else:
            if ordenamiento == 1:
                pass
                #ordenar por nombre
            
            elif ordenamiento == 2:
                
                for iteracion in range(len(paises)):
                    for item in paises:
                        if paises[iteracion]["poblacion"] < item["poblacion"]:
                            p = paises.index(item)
                            paises[iteracion], paises[p] = item, paises[iteracion]
                
                for item in paises:
                    print(f"{item["nombre"]} : {item["poblacion"]} hab.")


            elif ordenamiento == 3:
                for iteracion in range(len(paises)):
                    for item in paises:
                        if paises[iteracion]["superficie"] < item["superficie"]:
                            p = paises.index(item)
                            paises[iteracion], paises[p] = item, paises[iteracion]
                
                for item in paises:
                    print(f"{item["nombre"]} : {item["superficie"]} Km2")
            else:
                break




#GUARDAR Y SALIR

def guardar():
    with open("paises.csv", "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writeheader()
        escritor.writerows(paises)




#ARMAR EL PROGRAMA

def programa_principal():
    while True:
        eleccion = menu_principal()

        if eleccion == 1:
            ver_datos()

        elif eleccion == 2:
            agregar_pais()
        
        elif eleccion == 3:
            actualizar_datos()
        
        elif eleccion == 4:
            print(buscar()) #hay que decorar esto

        elif eleccion == 5:
            ver_estadisticas()

        elif eleccion == 6:
            ordenar()

        else:
            guardar()
            break

programa_principal()