import re
from claseAlumno import Alumno

class ManejadorAlumnos:
    #Atributos
    __lista = []
    __anios = ['primero','segundo','tercero','cuarto','quinto','sexto'] #años de una escuela
    __divisiones = ['a','b','c'] #Divisiones de los cursos

    #Metodos
    def __init__(self,list=[]):
        self.__lista = list
    

    def cargarAlumno(self,nom,an,div,cantI):
        #Valido tipo de datos
        if type(nom)==str and type(an)==str and type(div)==str and type(cantI)==int:
            #Compruebo que el nombre solo tenga letras
            if re.search('[\d]',nom) == None:
                #Compruebo que el año y la division correspondan a los que tiene la escuela
                if an.lower() in self.__anios and div.lower() in self.__divisiones:
                    newAlumno = Alumno(nom,an,div,cantI)
                    self.__lista.append(newAlumno)
                else:
                    print('Error: El año o la division ingresada no existen.')
            else:
                print('Error: El nombre no puede contener numeros')
        else:
            print('Error: El alumno no puede crearse, tipo de datos incorrecto.')


    def buscarAlumnos(self,anio,div):
        listaAlumnos = []
        inMax = Alumno.getInasMax()
        for alumno in self.__lista:
            if alumno.getAnio() == anio.lower() and alumno.getDivision() == div.lower():
                cantIn = alumno.getCantIn()
                if cantIn > inMax:
                    nombre = alumno.getNom()
                    '''Resto el 100% para determinar el porcentaje
                    por encima de las permitidas que tiene el alumno
                    ya que todos daran > 100% porque que superan la cantidad
                    de inasistencias maximas permitidas'''
                    porc = round((cantIn / inMax) * 100.0 - 100,2)
                    listaAlumnos.append([[nombre,porc]])
        
        if len(listaAlumnos) == 0:
            print('No se encontraron coincidencias.')
            return None
        else:
            return listaAlumnos


    def setMaxIn(self,newInasMax):
        error = False
        if type(newInasMax) == int and newInasMax >0: #Debe ser mayor a 0
            Alumno.inasMax = newInasMax
        else:
            error = True #Hay error en la carga
        return error 