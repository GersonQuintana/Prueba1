import paquetes.Analizar_Archivo as AA 
import xml.etree.ElementTree as ET
import Generar_Grafo 

opcion = 0
analizar_archivo = ""
ruta = ""
while (opcion != 6):

    print("\n############### Menú Principal ###############\n"
            "#      1. Cargar archivo                     #\n"
            "#      2. Procesar archivo                   #\n"
            "#      3. Escribir archivo de salida         #\n"
            "#      4. Mostrar datos del estudiante       #\n"
            "#      5. Generar gráfica                    #\n"
            "#      6. Salir                              #\n"
            "##############################################\n")

    
    try:
        opcion = int(input("Ingrese la opción a realizar: "))

        # Generando una excepción si la opción ingresada no está disponible
        if (opcion <= 0 or opcion >= 7):
            opcion = opcion/0
    except:
        print("\n----------------------------------------------")
        print("La opción ingresada no está disponible.\nVuelve a intentar.")
        print("----------------------------------------------\n")

    if (opcion == 1):
        #ruta = input("Ingrese ruta del archivo: ")
        ruta = "Prueba.xml"
        analizar_archivo = AA.Analizar(ruta)                # Creando un objeto de la clase Analizar_Archivo y enviando la ruta del archivo a constructor de la clase para estar ya listo a realizar las opciones otras opciones 

    
    elif (opcion == 2):
        try:
            if (ruta != ""):                                    # Validando que se haya ingresado un archivo
                repetido = analizar_archivo.analizar_file()     # Con el metodo analizar_archivo se valida que no hayan dos o mas matrices con el mismo nombre
                if (repetido == False):                         # Si no hay matrices con nombre repetido
                    analizar_archivo.obtener_matrices()      
        except:
            print()   
        
    
    elif (opcion == 3):
        try:
            analizar_archivo.escribir_archivo_de_salida()
        except:
            print()
            # Se va a imprimir algo dependiendo de la causa

    elif (opcion == 4):
        print("\n-------------------------------------------------------------")
        print("Gerson Sebastian Quintana Berganza\n"
              "201908686\n"
              "Introducción a la Programación y Computación 2, sección E\n"
              "Ingeniería en Ciencias y Sistemas\n"
              "4to Semestre")
        print("\n-------------------------------------------------------------\n")
    
    elif (opcion == 5):
        grafo = Generar_Grafo.Grafo(ruta)
        print()
        while (True):
            print("\n-------------------------------------------------------------")
            print("Matrices ingresadas: ")
            tamano = grafo.mostrar_matrices_disponibles()
            print("     " + str(tamano+1) + ". Volver al menú principal" )
            print("-------------------------------------------------------------\n")
            opcion_grafo = int(input("Ingrese el número correspondiente a la matriz que desee graficar: "))
            if (opcion_grafo >= 1 and opcion_grafo <= tamano):
                grafo.generar_grafo(opcion_grafo-1)
                break
            elif (opcion_grafo == tamano + 1):
                break

            else: 
                print("\nLa opcion que ingresó no esta disponible.")
                print("Vuelva a ingresar una opción")

        
        