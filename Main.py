# request permite hacer peticiones a una API o recuperar datos recibidos
from flask import Flask, request
from Analizadores.Sintactico import parser, getListaEstudiantes, getListaTareas
from Estructuras.ArbolAVL.TreeAVL import TreeAVL

from Estructuras.ArbolAVL.GrafoTreeAVL import GrafoABB


# El objeto app proporciona un decorador para alterar la vista que se desea
app = Flask(__name__)
treeavl = None
grafoavl = None

# Carga masiva
@app.route('/carga', methods=['POST'])
def carga_masiva():
    global treeavl, grafoavl
    if treeavl == None:
        treeavl = TreeAVL()
    if grafoavl == None:
        grafoavl = GrafoABB()
    tipo = request.json['tipo']
    path = request.json['path']    
    # # Lectura del archivo
    f = open(path, "r",encoding="UTF-8")
    content = f.read()
    f.close()
    parser.parse(content)
    lista_estudiantes = getListaEstudiantes()
    lista_tareas = getListaTareas()
    for estudiante in lista_estudiantes:
        treeavl.insertar(estudiante)
    for tareas in lista_tareas:
        print(tareas.getNombre())
    treeavl.recorridoEnOrden()
    grafoavl.graficarArbol(treeavl)
    return {"exit": "Gracias"}

# CRUD DE ESTUDIANTES
@app.route('/estudiante', methods=['POST', 'GET'])
def crud_estudiantes():
    global treeavl, grafoavl
    if treeavl == None:
        treeavl = TreeAVL()
    if grafoavl == None:
        grafoavl = GrafoABB()
    # Modificar un estudiante
    if request.method == "POST":
        print(request.json)
        treeavl.crear_estudiante(request.json)
        grafoavl.graficarArbol(treeavl)
        treeavl.recorridoEnOrden()
    elif request.method == "GET":
        print("El un get")
    return {"exit": "LLego con exito"}


if __name__ == "__main__":
    app.run(port=3000, debug=True)
    
