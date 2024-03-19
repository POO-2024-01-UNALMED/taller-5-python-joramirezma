class Zoologico():
    def __init__(self,nombre,ubicacion,zonas=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
        if zonas==None:
            zonas=[]
        self._zonas=zonas

    def setNombre(self,nombre):
        self._nombre=nombre

    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion

    def setZonas(self,zonas):
        self._zonas=zonas

    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZona(self):
        return self._zonas

    def cantidadTotalAnimales(self):
        contador=0
        for zona in self._zonas:
            contador += zona.cantidadAnimales()
        return contador
    
    def agregarZonas(self,*args):
        for i in args:
            self._zonas.append(i)