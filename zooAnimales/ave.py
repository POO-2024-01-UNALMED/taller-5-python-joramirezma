from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    
    def __init__(self, nombre="",edad=0,habitat="",genero="",colorPlumas=""):
        super().__init__(nombre,edad,habitat,genero,zona=None)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    @classmethod
    def setHalcones(cls,halcones):
        cls.halcones=halcones

    @classmethod
    def setAguilas(cls,aguilas):
        cls.aguilas=aguilas

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def getHalcones(cls):
        return cls.halcones
    
    @classmethod
    def getAguilas(cls):
        return cls.aguilas
    
    def setColorPlumas(self,colorPlumas):
        self._colorPlumas=colorPlumas

    def getColorPlumas(self):
        return self._colorPlumas

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        Ave.halcones += 1
        return cls(nombre,edad,"montanas",genero,"cafe glorioso")

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        Ave.aguilas += 1
        return cls(nombre,edad,"montanas",genero,"blanco y amarillo")

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)