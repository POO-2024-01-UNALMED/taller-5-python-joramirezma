from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre="",edad=0,habitat="",genero="",zona=None,colorEscamas="",largoCola=0):
        super().__init__(nombre,edad,habitat,genero,zona)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    @classmethod
    def setIguanas(cls,iguanas):
        cls.iguanas=iguanas

    @classmethod
    def setSerpientes(cls,serpientes):
        cls.serpientes=serpientes

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def getIguanas(cls):
        return cls.iguanas
    
    @classmethod
    def getSerpientes(cls):
        return cls.serpientes
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas

    def setLargoCola(self,largoCola):
        self._largoCola=largoCola

    def getColorEscamas(self):
        return self._colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    @classmethod
    def crearIguana(cls,nombre,edad,genero,zona=None):
        Reptil.iguanas += 1
        return cls(nombre,edad,"humedal",genero,zona,"verde",3)

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero,zona=None):
        Reptil.serpientes += 1
        return cls(nombre,edad,"jungla",genero,zona,"blanco",1)
    
    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)
