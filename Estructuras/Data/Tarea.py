
class Tarea:
    def __init__(self):
        self.carnet = 0
        self.nombre = ""
        self.descripcion = ""
        self.materia = ""
        self.fecha = ""
        self.hora = 0
        self.estado = ""

    def setCarnet(self, carnet):
        self.carnet = carnet
    
    def getCarnet(self):
        return self.carnet
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion
    
    def getDescripcion(self):
        return self.descripcion

    def setMateria(self, materia):
        self.materia = materia
    
    def getMateria(self):
        return self.materia
    
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def getFecha(self):
        return self.fecha
    
    def setHora(self, hora):
        self.hora = hora
    
    def getHora(self):
        return self.hora
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado