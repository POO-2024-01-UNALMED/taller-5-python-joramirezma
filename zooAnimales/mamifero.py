from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre="",edad=0,habitat="",genero="",pelaje=False,patas=0):
        super().__init__(nombre,edad,habitat,genero,zona=None)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    @classmethod
    def setCaballos(cls,caballos):
        cls.caballos=caballos

    @classmethod
    def setLeones(cls,leones):
        cls.leones=leones

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def getCaballos(cls):
        return cls.caballos
    
    @classmethod
    def getLeones(cls):
        return cls.leones
    
    def setPatas(self,patas):
        self._patas=patas
        
    def getPatas(self):
        return self._patas
    
    def setPelaje(self,pelaje):
        self._pelaje=pelaje

    def isPelaje(self):
        return self._pelaje
    
    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        Mamifero.caballos += 1
        return cls(nombre,edad,"pradera",genero,True,4)
    
    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        Mamifero.leones += 1
        return cls(nombre,edad,"selva",genero,True,4)
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero._listado)
    
    