class Alumno:
    #variables de clase
    inasMax = 5
    cantTotalClases = 7

    #variables de instancia
    __nombre = ''
    __anio = ''
    __division = ''
    __cantInas = 0

    def __init__(self,nom='',an='',div='',cantI=0):
        self.__nombre = nom
        self.__anio = an
        self.__division = div
        self.__cantInas = cantI
    
    #Metodos de instancia
    def getAnio(self):
        return self.__anio

    def getDivision(self):
        return self.__division
    
    def getCantIn(self):
        return self.__cantInas

    def getNom(self):
        return self.__nombre

    #Metodos de clase
    @classmethod
    def getInasMax(cls):
        return cls.inasMax
