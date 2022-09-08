from Lista_Simple import lista_simple
from matriz import Matriz


class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None
        self.anterior = None

class doubleList:
    def __init__(self):
        self.root = None
    


    def comparar_matrices(self,tamaño):
        apunta=self.root
        m_inicial=apunta.elemento

        a=""#patron de la primera matriz
        n=0#patron donde cambia

        for i in range(tamaño):
            for j in range(tamaño):
                a+=str(m_inicial.obtener_celda(i,j).elemento)
       
    

        while apunta.siguiente is not None:
            n+=1
            m_comparar=apunta.siguiente.elemento
            b=""#patron de la matriz a comp
            for i in range(tamaño):
                for j in range(tamaño):
                    b+=str(m_comparar.obtener_celda(i,j).elemento)
            apunta=apunta.siguiente        
            
            if a != b:#no coincide el patron
                return n
            else:
                return "bandera" #todas son iguales   

            
            

        
    def insertar_final(self, dato):

        if self.root is None:
            nuevoNodo = Nodo(dato)
            self.root = nuevoNodo
            return
        
        apuntador = self.root

        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente

        nuevoNodo = Nodo(dato)
        apuntador.siguiente = nuevoNodo
        nuevoNodo.anterior = apuntador

    def imprimir_listaD(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento, "→")
                apuntador = apuntador.siguiente

    def lista_vacia(self):
        if self.root is None:
            return True
        else:
            return False
    
    def contar_elementos(self):
        apuntador = self.root
        cuenta = 0

        while apuntador is not None:
            cuenta = cuenta + 1
            apuntador = apuntador.siguiente
        return cuenta
    def obtener_nodo(self,id):
        i=0
        apunt=self.root
        while apunt is not None:
            i+=1
            if i==id:
                return apunt.elemento
            apunt=apunt.siguiente    