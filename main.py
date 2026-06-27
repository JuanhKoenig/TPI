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
    lector = csv.DictReader(archivo)

    next(lector)

    for linea in archivo:
        print(linea)
        paises.append({"nombre" : linea[0], "poblacion" : linea[1], "superficie": linea[2], "continente" : linea[3]})



#MENU

def menu_principal(eleccion):

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

def agregar_pais():
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
                print("Error desconocido\n")

        else:
            print(f"nombre del pais registrado exitosamente: {pais_nuevo}\n")
            break
    
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
            break
    
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



        

