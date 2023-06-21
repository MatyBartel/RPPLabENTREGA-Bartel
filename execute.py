
from functions import *
import os

while True:
    os.system("cls")
    match(menu()):
        case 1:
            try:
                lista_diccionario =  cargar_archivo(nombre_archivo=input("-Ingrese direccion del archivo a usar 'carpeta//ejemplo.csv' :"))      # Parcial//insumos.csv
                lista_campo_agregado = agregar_campo_a_diccionarios(lista_diccionario,"stock")
                print("-LISTA CON CAMPO AGREGADO: STOCK-")
                mostrar_diccionarios(lista_campo_agregado)
            except FileNotFoundError:
                print("ERROR: El archivo que ingreso no existe, ingrese la direccion correctamente.")
            os.system("pause")
            os.system("cls")
        case 2:
            try: 
                insumos_por_marca = mostrar_dos_claves(lista_campo_agregado,"marca","stock")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 3:            
            try: 
                diccionario_filtrado = mostrar_tres_claves(lista_campo_agregado,"marca","nombre","precio")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 4:
            try: 
                lista_filtrada=buscar_por_caracteristica(lista_diccionario,caracteristica_ingresada=input("Ingrese caracteristica:"))
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("pause")
            os.system("cls")
        case 5:
            try: 
                lista_ordenada = ordenar_lista(lista_campo_agregado,"marca","precio")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 6:
            try: 
                marcas = mostrar_dos_claves(lista_campo_agregado,"marca","stock")
                carrito = comprar(lista_campo_agregado)
                if carrito != []:
                    archivo_texto = generar_archivo_txt(carrito,"carrito.txt")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("pause")
            os.system("cls")
        case 7:
            try:
                guardar_JSON(lista_campo_agregado,"./archivo_nuevo.json")
                print("ARCHIVO GUARDADO CON EXITO")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1,6)")
            os.system("pause")
            os.system("cls")

        case 8:
            try:
                json_leido = leer_JSON("./archivo_nuevo.json")
            except FileNotFoundError:
                print("EL ARCHIVO NO SE GENERO TODAVIA (punto 7)")
            os.system("pause")
            os.system("cls")

        case 9:
            try:
                resultado = list(map(aplicar_aumento,lista_campo_agregado))
                mostrar_diccionarios(resultado)
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("pause")
            os.system("cls")

        case 10:
            seguir_salir()

#---------------------------------- EXTRAS ------------------------------------------- 

        case 11:
            try:
                lista_con_agregados = agregar_producto(lista_campo_agregado)
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("pause")
            os.system("cls")

        case 12:
            try:
                guardar_json_o_csv=input("Ingrese como quiere guardar (json/csv):")
                direccion_archivo_nuevo = input("Ingrese direccion y nombre al final como quiera guardar el archivo: EJ: ./nuevo_archivo.formato:")
                guardar_json_csv(lista_con_agregados,direccion_archivo_nuevo,guardar_json_o_csv)
            except NameError:
                print("ERROR: Primero debe agregar productos, si no use la opcion 7")
                os.system("pause")
                os.system("cls")

        case _:
            print("Ingrese opcion valida")
