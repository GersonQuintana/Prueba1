
# Sintactico para Fase 2
from Estructuras.Data.Estudiante import Estudiante
from Analizadores.Lexico import tokens 
from Estructuras.Data.Estudiante import Estudiante
from Estructuras.Data.Tarea import Tarea

# Diccionario de nombres
# dictionary of names
names = {}
tipo = ""
lista_estudiantes = []
estudiante = None
lista_tareas = []
tarea = None

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'
    global tarea, estudiante
    if estudiante != None:
        insertarEstudiante(estudiante)
        estudiante = None
    if tarea != None:
        insertarTarea(tarea)
        tarea = None

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    global tipo, estudiante, tarea
    if t[3].lower() == "\"user\"":
        tipo = "user"
        estudiante = Estudiante()
    elif t[3].lower() == "\"task\"":
        tipo = "task"
        tarea = Tarea()
    

def p_items(t):
    """items : items item
             | item
    """

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    global tipo, estudiante, tarea
    if tipo == "user":
        if t[3].lower() == "carnet": # Si el carnet no esta coorecto, se omite este estudiante
            try:
                carnet_int = int(t[5].replace("\"", ""))
                estudiante.setCarnet(carnet_int)
            except ValueError:
                print("**************************************************************")
                print("Error de tipo en el carnet del nuevo estudiante. No se guardó.")
                print("**************************************************************")
                print("No se insertara el estudiante con carnet ", t[5])
                return 0
        elif t[3].lower() == "dpi":
            estudiante.setDPI(t[5])
        elif t[3].lower() == "nombre":
            estudiante.setNombre(t[5])
        elif t[3].lower() == "carrera":
            estudiante.setCarrera(t[5])
        elif t[3].lower() == "password":
            estudiante.setPassword(t[5])
        elif t[3].lower() == "creditos":
            estudiante.setCreditos(t[5])
        elif t[3].lower() == "edad":
            estudiante.setEdad(t[5])
        elif t[3].lower() == "correo":
            estudiante.setCorreo(t[5])
    elif tipo == "task":
        if t[3].lower() == "carnet":
            tarea.setCarnet(t[5])
        elif t[3].lower() == "nombre":
            tarea.setNombre(t[5])
        elif t[3].lower() == "descripcion":
            tarea.setDescripcion(t[5])
        elif t[3].lower() == "materia":
            tarea.setMateria(t[5])
        elif t[3].lower() == "fecha":
            tarea.setFecha(t[5])
        elif t[3].lower() == "hora":
            tarea.setHora(t[5])
        elif t[3].lower() == "estado":
            tarea.setEstado(t[5])

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    # Guardando el lexema que esta en el lado derecho de la produccion en lo que esta a lado izquierdo de la produccion
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                | TCORREO
                """
    # Guardando el lexema que esta en el lado derecho de la produccion en lo que esta a lado izquierdo de la produccion
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

# Quita las "" del carnet y lo convierte en un tipo de dato int
def strToInt(carnet):
    # VALIDAR QUE NO HAYA UN ERROR DE CONVERSION
    print("El carnet a convertir es ", carnet)
    
    return carnet


# def insertarEstudiante(carnet=None, dpi=None, nombre=None, carrera=None, password=None, creditos=None, edad=None, correo=None):
def insertarEstudiante(estudiante):
    global lista_estudiantes
    lista_estudiantes.append(estudiante)

def insertarTarea(tarea):
    global lista_tareas
    lista_tareas.append(tarea)

def getListaEstudiantes():
    global lista_estudiantes
    return lista_estudiantes

def getListaTareas():
    global lista_tareas
    return lista_tareas


import ply.yacc as yacc
parser = yacc.yacc()