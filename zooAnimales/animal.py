
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
    
    def toString(self):
        if (self._zona != None):
            return "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero) + ", la zona en la que me ubico es " + str(self._zona) + ", en el " + str(self._zona.getZoo().getNombre())
        else:
            return "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + ", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero)
        
    @staticmethod
    def totalPorTipo():
        from zooAnimales.ave import Ave
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil

        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\nAves : " + str(Ave.cantidadAves()) + "\nReptiles : " + str(Reptil.cantidadReptiles()) + "\nPeces : " + str(Pez.cantidadPeces()) + "\nAnfibios : " + str(Anfibio.cantidadAnfibios())