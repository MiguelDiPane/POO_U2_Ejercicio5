import csv
import time
from claseManejadorAlumno import ManejadorAlumnos
from claseMenu import Menu

def test():
    print('FUNCION TEST PARA CREAR ALUMNO')
    manejadorTest = ManejadorAlumnos()
    time.sleep(0.5)    
    print('Nombre y apellido con numero: ')
    manejadorTest.cargarAlumno('Manuel 34 Ortega','primero','a',10)
    time.sleep(0.5)
    print('Cantidad inasistencias no es numero entero: ')
    manejadorTest.cargarAlumno('Carlos Gomez','primero','a',12.4)
    time.sleep(0.5)
    print('Año no corresponde a rango entre primero y sexto: ')
    manejadorTest.cargarAlumno('Roberto Martinez','curso','b',3)
    time.sleep(0.5)
    print('Division no corresponde a rango entre a y c:')
    manejadorTest.cargarAlumno('Miriam Tello','segundo','z',2)
    time.sleep(0.5)
    print('Carga alumno con datos correctos.')
    manejadorTest.cargarAlumno('Lorenzo Fernandez','Tercero','B',3)
    del manejadorTest
    input('Test finalizado, presione ENTER para continuar...')


if __name__ == '__main__':
    #Manejador de alumnos
    manejador = ManejadorAlumnos()

    #Lectura archivo alumnos
    nomArch = 'alumnos.csv'
    print('Lectura de archivo: {}'.format(nomArch))
    archivo = open(nomArch)
    reader = csv.reader(archivo,delimiter=',')
    bandera = True


    for fila in reader:
        if bandera:
            bandera = False
        else:
            nombre = fila[0]
            anio = fila[1]
            division = fila[2]
            cantIn = int(fila[3])
            manejador.cargarAlumno(nombre,anio,division,cantIn)
    
    input('Presione ENTER para continuar...')
    #Actividad 2
    miMenu = Menu()
    miMenu.define_menu(['[1]- Actividad a','[2]- Actividad b','[3]- Funcion test','[0]- Salir'])
    miMenu.showMenu()
    op = miMenu.selectOption()
    
    while op != 0:
        if op == 1:
            anio = input('Ingrese año: ')
            division = input('Ingrese division: ')
            alumnos = manejador.buscarAlumnos(anio,division)
            if alumnos != None:
                encabezado = ['Alumno','Porcentaje']
                print('{:35}{:10}'.format(encabezado[0],encabezado[1]))
                for alumno in alumnos:
                    print('{:30}{:10}%'.format(alumno[0][0],alumno[0][1]))
            input('Presione ENTER para continuar...')
        elif op == 2:
            print('Modificar CANTIDAD INASISTENCIAS MAXIMA PERMITIDAS.')
            newCant = int(input('Ingrese cantidad: '))
            error = manejador.setMaxIn(newCant)
            if error == False:
                print('Modificacion realizada con exito!')
            else:
                print('Error: No se pudo realizar la modificacion')

            input('Presione ENTER para continuar...')
        elif op == 3:
            test()

        miMenu.showMenu()
        op = miMenu.selectOption()
