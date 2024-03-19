from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    
    def __init__(self, nombre="",edad=0,habitat="",genero="",colorEscamas="",cantidadAletas=0):
        super().__init__(nombre,edad,habitat,genero,zona=None)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
        

    @classmethod
    def setListado(cls,listado):
        cls._listado = listado

    @classmethod
    def setSalmones(cls,salmones):
        cls.salmones=salmones

    @classmethod
    def setBacalaos(cls,bacalaos):
        cls.bacalaos=bacalaos

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def getSalmones(cls):
        return cls.salmones
    
    @classmethod
    def getBacalaos(cls):
        return cls.bacalaos
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas

    def setCantidadAletas(self,cantidadAletas):
        self._cantidadAletas=cantidadAletas

    def getColorEscamas(self):
        return self._colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
        
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        Pez.salmones += 1
        return cls(nombre,edad,"oceano",genero,"rojo",6)

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        Pez.bacalaos += 1
        return cls(nombre,edad,"oceano",genero,"gris",6)

    @classmethod
    def cantidadPeces(cls):
        return len(Pez._listado)