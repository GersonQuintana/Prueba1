import xml.etree.ElementTree as ET
from graphviz import Digraph
from graphviz import render
import os

class Grafo:

    def __init__(self, ruta):
        self.ruta = ruta
        self.s = Digraph('structs', filename='grafo.dot', node_attr={'shape': 'plaintext'})
        self.s.attr(bgcolor='gray', fontcolor='white')
        self.tree = ET.parse(ruta)
        self.root = self.tree.getroot()

        self.i_de_tabla = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'''
        self.f_de_tabla = '''</TABLE>>'''
        self.i_de_fila = '<TR>'
        self.f_de_fila = '</TR>'
        self.i_de_columna = '<TD PORT="f0">'
        self.f_de_columna = '</TD>'

    # Va a retornar el numero de matrices que se pueden graficar
    def cantidad_de_matrices(self):
        tamano = 0
        for i in range(len(self.root)):
            tamano += 1
        return tamano

    # Muestra las matrices disponibles para graficar
    def mostrar_matrices_disponibles(self):
        tamano = 0
        for i in range(len(self.root)):
            print("     " + str(i+1) + ". " + self.root[i].get("nombre"))
            tamano += 1
        return tamano


    # Como lo que voy a mostrar las matrices del documento, y cada una de ellas se les asocio un numero
    # cuando el usuario ingrese el numero, en realidad lo que esta mandando es la posicion de esa matriz dentro
    # del arbol
    def generar_grafo(self, opcion_grafo):

        self.s.node('struct1', '''<
                <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" PORT="f0"><TR>
                    <TD>MATRICES</TD>
                </TR>
                </TABLE>>''')

        grafo = self.root[opcion_grafo]

        nombre = self.i_de_fila + self.i_de_columna + grafo.get("nombre") + self.f_de_columna + self.f_de_fila
        tabla = self.i_de_tabla + nombre + self.f_de_tabla
        self.s.node('struct2', tabla)

        n = self.i_de_fila + self.i_de_columna + "n = " + grafo.get("n") + self.f_de_columna + self.f_de_fila
        tabla = self.i_de_tabla + "n = " + n + self.f_de_tabla
        self.s.node('struct3', tabla)

        m = self.i_de_fila + self.i_de_columna + "m = " + grafo.get("m") + self.f_de_columna + self.f_de_fila
        tabla = self.i_de_tabla + m + self.f_de_tabla
        self.s.node('struct4', tabla)

        n = int(grafo.get("n"))  
        m = int(grafo.get("m"))      
        datos = grafo.findall("dato")

        tabla = self.i_de_tabla
        for i in range(n):      # Recorriendo las filas
            tabla += self.i_de_fila + "\n"
            for j in range(m):  # Recorreindo las columnas
                for l in range(len(datos)):
                    x = int(datos[l].get("x"))
                    y = int(datos[l].get("y"))
                    if (x == (i+1) and y == (j+1)):
                        dato = datos[l].text
                        tabla += self.i_de_columna + dato + self.f_de_columna + "\n"
            tabla += self.f_de_fila + "\n"
        tabla += self.f_de_tabla + "\n"

        #print("El formato es ", tabla)

        self.s.node('struct5', tabla)

        self.s.edges([('struct1:f0', 'struct2:f0'), ('struct2:f0', 'struct3:f0'), ('struct2:f0', 'struct4:f0'), ('struct2:f0', 'struct5:f0')])

        #print("El nombre del filename es ", self.s.filename)
        self.s.view()
        archivo = render('dot', 'png', 'grafo.dot')
        #print(archivo)
        os.system(archivo)

        


