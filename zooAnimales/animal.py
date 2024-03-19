import zooAnimales

class Animal():
    _totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero,zona=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal._totalAnimales += 1

    @classmethod
    def setTotalAnimales(cls,totalAnimales):
        cls._totalAnimales=totalAnimales

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    def setNombre(self,nombre):
        self._nombre=nombre

    def setEdad(self,edad):
        self._edad=edad

    def setHabitat(self,habitat):
        self._habitat=habitat

    def setGenero(self,genero):
        self._genero=genero

    def setZona(self,zona):
        self._zona=zona

    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def getGenero(self):
        return self._genero
    
    def getZona(self):
        return self._zona
    
    def __str__(self):
        if (self._zona != None):
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero
        
    @staticmethod
    def totalPorTipo():
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + "\nAves: " + Ave.cantidadAves() + "\nReptiles: " + Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() + "\nAnfibios: " + Anfibio.cantidadAnfibios