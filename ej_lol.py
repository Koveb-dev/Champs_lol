import time
import os
import csv


try:
    titulos = ["identificador", "nombre", "anio de lanzamiento"]
    with open("campeones_lol.csv", "x", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(titulos)
except:
    pass

print('Bienvenido a la app champs lol!')
time.sleep(1)
os.system('cls')

while True:
    time.sleep(1)
    os.system('cls')
    while True:
        print('\tMenú\t\n1. Agregar Campeón\t\n2. Ver campeones\t\n3. Salir')
        try:
            opc = int(input('Ingrese una opción: '))
            if opc in (1, 2, 3):
                break
            else:
                print('ERROR! debe ingresar una opción valida, opciones valida(1,2,3)!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar un número entero!')

    if opc == 1:
        print('Agregar campeón!')
        time.sleep(1)
        os.system('cls')
        while True:
            try:
                identificador = int(input('Ingrese id del campeón: '))
                if identificador >= 1 and identificador <= 168:
                    print('Id de campeón registrado!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print(
                        'ERROR! el id a ingresar debe estar dentro del rango de 1 a 168!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debe ingresar número entero!')

        while True:
            nombre = str(input('Ingrese el nombre del campeón: '))
            if len(nombre.strip()) >= 2:
                print('Nombre registrado exitosamente!')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print('ERROR! el nombre del campeón debe contener al menos 2 letras!')
            time.sleep(1)
            os.system('cls')

        while True:
            try:
                anio = int(
                    input('Ingrese el año de lanzamiento del campeón: '))
                if anio >= 2009 and anio <= 2024:
                    print('Año de lanzamiento registrado exitosamente!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print(
                        'ERROR! debe ingresar un año valido, el año debe estar dentro del rango de años 2009 a 2024!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debe ingresar números enteros!')

        campeon_agregar = [identificador, nombre, anio]

    elif opc == 2:
        pass

    else:
        for q in range(1, 4):
            print('Saliendo de app champs lol', ('.'*q))
            time.sleep(1)
            os.system('cls')
        break
