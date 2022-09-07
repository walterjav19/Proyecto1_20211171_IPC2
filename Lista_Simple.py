from paciente import *
class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class lista_simple:
    def __init__(self):
        self.root=None        

    def isempty_pacientes(self):
        if self.root is None:
            return True

    def add(self,midato):
        self.root=node(data=midato,next=self.root)

    def append(self,midato):
        if self.root is None:
            self.root=node(data=midato)
            return
        auxRoot=self.root
        while auxRoot.next !=None:
            auxRoot=auxRoot.next
        auxRoot.next=node(data=midato)            

    def imprimir_lista(self):
        nodeAux=self.root
        while nodeAux!=None:
            print('Nodo:',nodeAux.data)
            nodeAux=nodeAux.next
    
    def imprimir_lista_pacientes(self):
        nodeAux=self.root
        while nodeAux!=None:
            print("===Paciente===")
            print('Nombre:',nodeAux.data.get_nombre())
            print('Edad:',nodeAux.data.get_edad())
            print("")
        
            nodeAux=nodeAux.next
    
    def obtener_paciente(self,num):
        i=0
        nodeAux=self.root
        while nodeAux!=None:
            i+=1
            if num==i:
                return nodeAux.data
            nodeAux=nodeAux.next    



    def len(self):
        i=0
        nodeAux=self.root
        while nodeAux!=None:
            nodeAux=nodeAux.next
            i+=1
        return i

