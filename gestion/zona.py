class Zona():
    def __init__(self,nombre,zoo=None,animales=None):
        self._nombre=nombre
        self._zoo=zoo
        if animales == None:
            animales=[]
        self._animales=animales

    def setNombre(self,nombre):
        self._nombre=nombre

    def setZoo(self,zoo):
        self._zoo=zoo

    def setAnimales(self,animales):
        self._animales=animales

    def getNombre(self):
        return self._nombre
    
    def getZoo(self):
        return self._zoo
    
    def getAnimales(self):
        return self._animales
    
    def cantidadAnimales(self):
        return len(self._animales)
    
    def agregarAnimales(self,animal):
        self._animales.append(animal)