from xml.dom import minidom
import xml.etree.ElementTree as ET
import paquetes.lista_circular.Lista_Circular as lista_c
import paquetes.lista_circular.Lista_Enlazada as lista_e

class Analizar:

    def __init__(self, ruta):
        #print("Entro al constructor")
        self.ruta = ruta
        self.lista_circular = ""

    
    # Para verificar que no haya ningun nombre de alguna martriz dentro del archivo de entrada
    def analizar_file(self):
        tree = minidom.parse(self.ruta)                 # Generando un árbol
        matriz = tree.getElementsByTagName("matriz")    # Obteniendo todas la etiquetas con nombre "matriz"

        lista = lista_c.Lista_Circular()                # Objetos de la clase Lista_Circular

        # Obteniendo el valor del atributo nombre en las etiquetas matriz
        for i in matriz:
            lista.insertar(nombre_matriz=i.attributes['nombre'].value)  # Insertando todos los nombre de las matrices a una lista circular

        repetido = lista.comparar_nombres(len(matriz))  # repetido va a tomar el valor de False si no hay al menos una matriz con el mismo nombre, o True si no hay dos o mas matrices con el mismo nombre

        if (repetido == True):                          # Si hay una matriz repetida
            print("Existen al menos dos matrices con el mismo nombre. Intente modificando el archivo de entrada o ingresando uno diferente.")
            return True
        
        return False                                    # Va a retornar False si no hay matrices con el mismo nombre



    # Esta funcion va a ser la encargada de enviar los artributos y valores de los elementos que corresponden a cada matriz
    def obtener_matrices(self):
        tree = ET.parse(self.ruta)                      # Obteniendo un arbol
        root = tree.getroot()                           # Obteniendo la raiz del arbol (<matrices>)

        self.lista_circular = lista_c.Lista_Circular()  # Objeto de la modulo Lista_Circular
        
        for i in range(len(root)):                      # Recorriendo todos los subelementos de la raiz ( <matriz nombre="Ejemplo" n=4 m=4> ...  <matriz nombre="Ejempl_n" n=4 m=4>)
            nombre_matriz = root[i].get("nombre")       # Obteniendo el nombre de la matriz (Ejemplo)
            #print(nombre_matriz)
            n = int(root[i].get("n"))                   # Obteniendo el atributo n 
            m = int(root[i].get("m"))                   # Obteniendo el atributo m

            # Logica: Lo siguiente es primeto insertar la matriz, luego ir a obtener el objeto matriz del nodo correspondiente con la funcion matriz_a_llenar
            self.lista_circular.insertar(nombre_matriz=nombre_matriz, n=n, m=m)     # Insertando un nuevo nodo que contiene una matriz, el numero de filas (n) y el numero de columnas (m)
            datos = root[i].findall("dato")                                         # Obteniendo todos los elementos que tengan la etiquera dato (<dato x=1 y=1>2</dato>)
            matriz_a_llenar = self.lista_circular.matriz_a_llenar(nombre_matriz)    # Por medio del nombre se busca la matriz (que acaba de ser insertada) en donde se llenaran los datos
            #print("-------------------------------------------")
            #print("LLego aqui 1")

            if (len(datos) == (n * m)):                                             # Primero validando que el numero de datos a ingresar sea justo el numero de datos a permitidos dentro de la matriz

                count = 0
                for a in range(n):      # Recorriendo las filas
                    for b in range(m):  # Recorreindo las columnas
                        count = 0
                        for l in range(len(datos)):
                            x = int(datos[l].get("x"))
                            y = int(datos[l].get("y"))
                            valor = datos[l].text
                            if (x == (a+1) and y == (b+1)):                         # count aumentara en una unidad cuando encuentre una misma posicion
                                count += 1
                            if (count == 2):                                        # Si count llega a 2 significa que se esta intentando guardar dos elementos en una misma posicion, lo cual no es permitido         
                                # Significa que hay dos o mas elementos con la misma posicion
                                print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                print("\nSe intenta ingresar el valor " + valor + " en la posición (" + str(x) + ", " + str(y) + ")" + " la cual ya está ocupada por otro elemento.")
                                print("Modifique el documento de entrada ó ingrese uno nuevo.\n")
                                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                n = 7/0
                                

                for j in range(len(datos)):                                             # Recorriendo todas las etiquetas <dato> contenidas dentro de la matriz retornada (<matriz_a_llenar>)
                    #print("La matriz a llenar es ", matriz_a_llenar.nombre)
                    dato = int(datos[j].text)                                           # Obteniendo el texto contenido en la etiqueda dato (<dato x=1 y=2>3</dato>)
                    x_ = int(datos[j].get("x"))                                         # Obteniendo el atributo n contenido en la etiqueda dato (<dato x=1 y=2>3</dato>)
                    y_ = int(datos[j].get("y"))                                         # Obteniendo el atributo n contenido en la etiqueda dato (<dato x=1 y=2>3</dato>)


                    # Validando que la cantidad de elementos a ingresar sea igual al producto de n x m, esto para garantizar que se llenará por completo la matriz

                    #print("SE ENVIARA " + "(" + str(x_) + ", " + str(y_) + ")")
                    if (x_ <= n and x_ >= 1 and y_ <= m and y_ >= 1):
                        matriz_a_llenar.lista_enlazada.insertar__(dato, x_ - 1, y_ - 1)     # Debido a que el atributo x de la etiqueta empieza en 1, yo le resto 1 para que empiece en 0
                        if (dato == 0):                                                     # Si el dato es 0, el numero que va a tener en esa posicion dentro de la lista de valore es binario es 0
                            matriz_a_llenar.lista_enlazada.insertar_binaria(0, x_ - 1, y_ - 1)
                        else: 
                            matriz_a_llenar.lista_enlazada.insertar_binaria(1, x_ - 1, y_ - 1)  # De lo contrario sera un 1
                    else:
                        print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("\nSe intenta almacenar el valor " + str(dato) + " en la posición " + "(" + str(x_) + ", " + str(y_) + ")" + " la cual esta fuera del rango especificado por las filas/columnas en la matriz " + nombre_matriz)
                        print("Modifique el documento de entrada ó ingrese uno nuevo.\n")
                        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        n = 7/0
            else:
                if (len(datos) < (n * m)):
                    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\nEl número de elementos a ingresar en la matriz " + nombre_matriz + " es menor (" + str(len(datos)) + ") al permitido en esta (" + str(n*m) + "), por lo que la matriz no se podrá llenar por completo.")
                    print("Modifique el documento de entrada ó ingrese uno nuevo.\n")
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    n = 7/0
                else:
                    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("\nEl número de elementos a ingresar en la matriz " + nombre_matriz + " es mayor (" + str(len(datos)) + ") al permitido en esta (" + str(n*m) + "), por lo que la matriz revasará la cantidad de elementos.")
                    print("Modifique el documento de entrada ó ingrese uno nuevo.\n")
                    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                    n = 7/0
        

        #matriz_imprimir = self.lista_circular.imprimir_matriz_datos(root[0].get("nombre"))
        #print("Matriz: ", matriz_imprimir.nombre)
        #print("n == ", matriz_imprimir.n)
        #print("m == ", matriz_imprimir.m)
        #matriz_imprimir.lista_enlazada.imprimir_datos()
        #print("\n-------------------------------------")
        #matriz_imprimir.lista_enlazada.imprimir_binaria()
        #print()

        self.lista_circular.comparar_filas()
        #print("###########################################")
        #matrix = self.lista_circular.lista_CR.imprimir_matriz_datos(root[0].get("nombre"))
        matrix.lista_enlazada.imprimir_datos()
        print("###########################################")
        #lista_circular.mostrar_XML()
        #self.escribir_archivo_de_salida(lista_circular)


    def escribir_archivo_de_salida(self):
        #lista_circular.mostrar_XML()
        self.lista_circular.mostrar_XML()
        print("El archivo fue escrito con exito")