from Estructuras.Data.Estudiante import Estudiante

class NodoAVL:
    def __init__(self, estudiante):
        self.estudiante = estudiante # Data
        self.key = self.estudiante.getCarnet() # Obteniendo el key del estudiante que se acaba de insertar
        self.height = 1 # La atura inicial del nodo es 1
        self.izq = None
        self.der = None
    
    

class TreeAVL:
    def __init__(self):
        self.root = None
    
    # Retorna la altura del nodo
    def calcHeigth(self, nodo):
        # Si el nodo recibido el null
        if nodo == None:
            return 0
        return nodo.height
    
    # Calcula la maxima altura
    def maxHeight(self, a, b):
        if a > b:
            return a
        return b
    
    # Calcula el balance del subarbol
    def getBalance(self, nodo):
        if nodo == None:
            return 0
        return self.calcHeigth(nodo.der) - self.calcHeigth(nodo.izq)

    # Rotar a la derecha
    def rotarDerecha(self, n):
        n1 = n.izq
        t2 = n1.der
        # Rotar
        n1.der = n
        n.izq = t2
        # Acualizar las alturas
        n.height = self.maxHeight(self.calcHeigth(n.izq), self.calcHeigth(n.der)) + 1
        n1.height = self.maxHeight(self.calcHeigth(n1.izq), self.calcHeigth(n1.der)) + 1
        return n1

    # Rotar a la izquierda
    def rotarIzquierda(self, n):
        n1 = n.der
        t2 = n1.izq 
        # Rotar
        n1.izq = n
        n.der = t2
        # Actualizar alturas
        n.height = self.maxHeight(self.calcHeigth(n.izq), self.calcHeigth(n.der)) + 1
        n1.height = self.maxHeight(self.calcHeigth(n1.izq), self.calcHeigth(n1.der)) + 1
        return n1

    def insertar(self, estudiante):
        # self.insertarRec(raiz, key)
        self.root = self.insertarRec(self.root, estudiante)

    def insertarRec(self, root, estudiante):   
        # estudiante.getCarnet() devuelve la llave del nodo 
        if root == None:
            print("*******************************")
            print("Estudiante Insertado con éxito")
            print("*******************************")
            return NodoAVL(estudiante)
        elif estudiante.getCarnet() < root.estudiante.getCarnet():
            root.izq = self.insertarRec(root.izq, estudiante)
        elif estudiante.getCarnet() > root.estudiante.getCarnet():
            root.der = self.insertarRec(root.der, estudiante)
        else: # Es igual al key de root, por lo tanto no se inserta
            return root
        
        #Actualizar la altura del nodo
        root.height = self.maxHeight(self.calcHeigth(root.izq), self.calcHeigth(root.der)) + 1
        # Verificar el balance del nodo
        balance = self.getBalance(root)
        # ROTACIONES
        # Caso Izquierda Izquieda
        if balance < -1 and estudiante.getCarnet() < root.izq.estudiante.getCarnet():
            return self.rotarDerecha(root)
        # Caso Derecha Derecha
        if balance > 1 and estudiante.getCarnet() >  root.der.estudiante.getCarnet():
            return self.rotarIzquierda(root)
        # Caso Izquierda Derecha
        if balance < -1 and estudiante.getCarnet() > root.izq.estudiante.getCarnet():
            root.izq = self.rotarIzquierda(root.izq)
            return self.rotarDerecha(root)
        # Caso Derecha Izquierda
        if balance > 1 and estudiante.getCarnet() < root.der.estudiante.getCarnet():
            root.der = self.rotarDerecha(root.der)
            return self.rotarIzquierda(root)

        return root
    
    # Crear un estudiante
    def crear_estudiante(self, atributo_json):
        new_estudiante = Estudiante()
        try:
            if atributo_json["carnet"]:
                new_estudiante.setCarnet(int(atributo_json["carnet"]))
            if atributo_json["DPI"]:
                new_estudiante.setDPI(atributo_json["DPI"])
            if atributo_json["nombre"]:
                new_estudiante.setNombre(atributo_json["nombre"])
            if atributo_json["carrera"]:
                new_estudiante.setCarrera(atributo_json["carrera"])
            if atributo_json["correo"]:
                new_estudiante.setCorreo(atributo_json["correo"])
            if atributo_json["password"]:
                new_estudiante.setPassword(atributo_json["password"])
            if atributo_json["creditos"]:
                new_estudiante.setCreditos(atributo_json["creditos"])
            if atributo_json["edad"]:
                new_estudiante.setEdad(atributo_json["edad"])
        except ValueError:
            print("**************************************************************")
            print("Error de tipo en el carnet del nuevo estudiante. No se guardó.")
            print("**************************************************************")
            return 0
        self.insertar(new_estudiante)
        


    def recorridoEnOrden(self):
        self.recorridoEnOrdenRec(self.root)
    
    def recorridoEnOrdenRec(self, root):
        if root != None:
            self.recorridoEnOrdenRec(root.izq)
            print(root.estudiante.getCarnet(), " > ")
            self.recorridoEnOrdenRec(root.der)
