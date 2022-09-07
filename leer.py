from Lista_Simple import *
from paciente import *
import xml.etree.ElementTree as ET

objeto_lista_paciente=lista_simple()
class leer: 
    def leer_archivo(path):
        try:   
            nombre=""
            edad=""
            tree=ET.parse(path)
            root=tree.getroot()
            pacientes=len(root)
            for i in range(pacientes):
                for j in range(4):
                    if j==0:
                        for k in range(1):
                            nombre=root[i][j][k].text
                            edad=root[i][j][k+1].text
                    elif j==1:
                        periodos=root[i][j].text
                    elif j==2:
                        m=root[i][j].text
                    elif j==3:
                        celdas=root[i][j]
                objeto_paciente=paciente(nombre,edad,periodos,m,celdas)
                objeto_lista_paciente.append(objeto_paciente)
        except FileNotFoundError:
            print("")
            print("!!!!!Archivo inexistente!!!!")
            print("")


        

