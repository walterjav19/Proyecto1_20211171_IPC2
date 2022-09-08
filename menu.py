from re import T
from Lista_Simple import *
from generar_repo import repo
from leer import *
from lista_doble import doubleList
from paciente import *
from matriz import Matriz

opcion=0

def menu():
    global opcion
    print("===MENU DE INICIO===")
    print("1. elegir archivo xml")
    print("2. Gestionar pacientes")
    print("3. salir")
    opcion=input("")
    if int(opcion)==1:
        opcion_1()
    elif int(opcion)==2:
        opcion_2()
    elif int(opcion)==3:
        print("SALIENDO!!")    
    else:
        print("Por favor elija una opcion entre 1-3")       


def opcion_1():
    ruta=input("Ingrese la ruta de su archivo: ")
    leer.leer_archivo(ruta)

def opcion_2():
    vacia=objeto_lista_paciente.isempty_pacientes()
    if vacia==True:
        print("")
        print("Todavia no hay pacientes")
        print("")
    else:    
        objeto_lista_paciente.imprimir_lista_pacientes()
        pac=input("Cual paciente quiere analizar: ")
        mostras_pac(pac)
    
def mostras_pac(pac):
    print("")
    paciente_analizar=objeto_lista_paciente.obtener_paciente(int(pac))
    print("===PACIENTE ANALIZADO===")

    print("Nombre: "+paciente_analizar.get_nombre())
    print("Edad: "+paciente_analizar.get_edad())
    print("Periodos: "+paciente_analizar.get_periodos())
    print("Tamaño de la rejilla: "+str(paciente_analizar.get_m())+" X "+str(paciente_analizar.get_m()))
    print("")
    tamaño=int(paciente_analizar.get_m())
    periodos=int(paciente_analizar.get_periodos())
    matrix=Matriz()
    for i in range(tamaño):
        for j in range(tamaño):
            matrix.append(0,i,j)
    rejillas_contagiadas=paciente_analizar.get_contagiadas()
    matrix.setear_enfermas(rejillas_contagiadas)
    print("-----Estado inicial-----")
    matrix.imprimir_matriz(tamaño)   
    print("")
    a=input("Quiere comenzar con el analisis  [SI/NO]: ")
    a=a.lower()
    if a =="si":
        linked_list=doubleList()
        linked_list.insertar_final(matrix)
        i=0
        while i!=periodos:
            i+=1
            print("******* PERIODO "+str(i)+" *******")
            print("")
            nueva=matrix.actualizar_enfermas(tamaño)
            nueva.imprimir_matriz(tamaño)
            linked_list.insertar_final(nueva)
            matrix=nueva
            print("\n\n***********************************")
            print("")
        b=str(input("generar reporte [SI/NO] ")) 
        b=b.lower()
        if b=="si":
    
            c=linked_list.comparar_matrices(tamaño)
            if str(c)=="bandera":
                rep=repo(paciente_analizar.get_nombre(),paciente_analizar.get_edad(),paciente_analizar.get_periodos(),paciente_analizar.get_m(),"Grave",None)
                rep.crear_xml_grave()
                print("reporte generado revise su carpeta.....")
            elif c>0:
                rep=repo(paciente_analizar.get_nombre(),paciente_analizar.get_edad(),paciente_analizar.get_periodos(),paciente_analizar.get_m(),"Mortal",c)
                rep.crear_xml_mortal()
                print("reporte generado revise su carpeta.....")
            else:
                pass    
                 




    

    


while int(opcion) !=3 :
    menu()

    

