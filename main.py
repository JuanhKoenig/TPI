#1 Leer el CSV y cargarlo en una lista de diccionarios

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
    lector = csv.DictReader(archivo) #esto saltea los encabezados, entonces borre el next(lector)

    for linea in lector:
        print(linea)
        paises.append({"nombre" : linea["nombre"], "poblacion" : int(linea["poblacion"]), "superficie": int(linea["superficie"]), "continente" : linea["continente"]})



#MENU

def menu_principal():

    while True:
        try:
            eleccion = int(input("1)Ver Datos\n2)Agregar país\n3)Actualizar datos\n4)Buscar pais\n5)Estadisticas\n6)Salir\n"))

            if eleccion not in (1, 2, 3, 4, 5, 6):
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
                
        except ValueError as e:
            if str(e) == "repetido":
                print(f"Error, el pais {pais_nuevo} ya esta registrado en la lista\n")
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
            pais_nuevo_continente = int(input("Continente:\n1. Asia\n2. África\n3. América\n4. Antártida\n5. Europa\n6. Oceanía"))
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

            tipo_de_dato = int(input("Editar: \n1.Nombre\n2.Poblacion\n3.Superficie\n4.Continente"))

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

def mostrar_estadisticas(paises):
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
            