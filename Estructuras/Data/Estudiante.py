class Estudiante:
    def __init__(self):
        self.carnet = 0
        self.dpi = 0
        self.nombre = ""
        self.carrera = ""
        self.password = ""
        self.creditos = 0
        self.edad = 0
        self.correo = ""
    
    def setCarnet(self, carnet):
        self.carnet = carnet
    
    def getCarnet(self):
        return self.carnet
    
    def setDPI(self, dpi):
        self.dpi = dpi
    
    def getDPI(self):
        return self.dpi

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getNombre(self):
        return self.nombre

    def setCarrera(self, carrera):
        self.carrera = carrera
    
    def getCarrera(self):
        return self.carrera
        
    def setPassword(self, password):
        self.password = password
    
    def getPassword(self):
        return self.password
    
    def setCreditos(self, creditos):
        self.creditos = creditos
    
    def getCreditos(self):
        return self.creditos
    
    def setEdad(self, edad):
        self.edad = edad
    
    def getEdad(self):
        return self.edad

    def setCorreo(self, correo):
        self.correo = correo
    
    def getCorreo(self):
        return self.correo
