from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre="",edad=0,habitat="",genero="",zona=None,colorPiel="",venenoso=False):
        super().__init__(nombre,edad,habitat,genero,zona)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
        
        
    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    @classmethod
    def setRanas(cls,ranas):
        cls.ranas=ranas

    @classmethod
    def setSalamandras(cls,salamandras):
        cls.salamandras=salamandras

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def getRanas(cls):
        return cls.ranas
    
    @classmethod
    def getSalamandras(cls):
        return cls.salamandras
    
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel

    def setVenenoso(self,venenoso):
        self._venenoso=venenoso

    def getColorPiel(self):
        return self._colorPiel
    
    def isVenenoso(self):
        return self._venenoso
    
    @classmethod
    def crearRana(cls,nombre,edad,genero,zona=None):
        Anfibio.ranas += 1
        return cls(nombre,edad,"selva",genero,zona,"rojo",True)

    @classmethod
    def crearSalamandra(cls,nombre,edad,genero,zona=None):
        Anfibio.salamandras += 1
        return cls(nombre,edad,"selva",genero,zona,"negro y amarillo")

    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)

