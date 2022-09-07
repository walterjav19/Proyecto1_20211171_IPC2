


class Nodo_matriz:

    def __init__(self, elemento,fila,columna):
        self.elemento = elemento
        self.fila=fila
        self.columna=columna
        self.siguiente = None
        self.anterior = None

    def get_fila(self):
        return self.fila

    def get_columna(self):
        return self.columna


class Matriz:
    def __init__(self):
        self.root = None



    def insertar_lista_vacia(self, dato,fila,columna):
        if self.root is None:
            nuevoNodo = Nodo_matriz(dato,fila,columna)
            self.root = nuevoNodo
        else:
            print("La lista no esta vacia")
    
    def add(self, dato,fila,columna):

        if self.root is None:
            self.insertar_lista_vacia(dato,fila,columna)
        else:
            nuevoNodo = Nodo_matriz(dato,fila,columna)
            nuevoNodo.siguiente = self.root
            self.root.anterior = nuevoNodo
            self.root = nuevoNodo
    
    def append(self, dato,fila,columna):

        if self.root is None:
            nuevoNodo = Nodo_matriz(dato,fila,columna)
            self.root = nuevoNodo
            return
        
        apuntador = self.root

        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente

        nuevoNodo = Nodo_matriz(dato,fila,columna)
        apuntador.siguiente = nuevoNodo
        nuevoNodo.anterior = apuntador
    
    def insertar_despues_elemento(self, x, dato,fila,columna):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:

                if apuntador.elemento == x:
                    break
                apuntador = apuntador.siguiente
            
            if apuntador is None:
                print("El elemento no se encuentra en la lista")
            else:
                nuevoNodo = Nodo_matriz(dato,fila,columna)
                nuevoNodo.anterior = apuntador
                nuevoNodo.siguiente = apuntador.siguiente
                if apuntador.siguiente is not None:
                    apuntador.siguiente.anterior = nuevoNodo
                apuntador.siguiente = nuevoNodo
    
    def insertar_antes_elemento(self, x, dato,fila,columna):
        if self.root is None:
            print("La lista esta vacia")
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento == x:
                    break
                apuntador = apuntador.siguiente
            
            if apuntador is None:
                print("Elemento no se encuentra en la lista")
            else:
                nuevoNodo = Nodo_matriz(dato,fila,columna)
                nuevoNodo.siguiente = apuntador
                nuevoNodo.anterior = apuntador.anterior

                if apuntador.anterior is not None:
                    apuntador.anterior.siguiente = nuevoNodo
                apuntador.anterior = nuevoNodo

    def imprimir_lista(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento, end="→")
                apuntador = apuntador.siguiente
            print("null")    

    def lista_vacia(self):
        if self.root is None:
            return True
        else:
            return False
    
    def contar_elementos(self):
        apuntador = self.root
        cuenta = 0

        while apuntador is not None:
            cuenta += 1
            apuntador = apuntador.siguiente
        return cuenta
    
    def eliminar_inicio(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None

        self.root = self.root.siguiente
        self.root.anterior = None
    
    def eliminar_final(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None
            return

        apuntador = self.root
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        apuntador.anterior.siguiente = None
    
    def eliminar_elemento(self, x):
        if self.root is None:
            print("La lista esta vacia")
            return
        
        if self.root.siguiente is None:
            if self.root.elemento == x:
                self.root = None
            else:
                print("Elemento no encontrado")
        
        if self.root.elemento == x:
            self.eliminar_inicio()
            return
        
        apuntador = self.root
        while apuntador.siguiente is not None:
            if apuntador.elemento == x:
                break
            apuntador = apuntador.siguiente
        
        if apuntador.siguiente is not None:
            apuntador.anterior.siguiente = apuntador.siguiente
            apuntador.siguiente.anterior = apuntador.anterior
        else:
            if apuntador.elemento == x:
                self.eliminar_final()
            else:
                return print("Elemento no encontrado")

    def imprimir_matriz(self,tamaño):
        i=-1
        apuntador = self.root
        while apuntador is not None:
            i+=1
            if i==tamaño:
                print("")
                print(apuntador.elemento,end=" ")
                i=0
            else:    
                print(apuntador.elemento, end=" ")
            apuntador = apuntador.siguiente


    def imprimir_atributos(self,tamaño):
        i=-1
        apuntador = self.root
        while apuntador is not None:
            i+=1
            if i==tamaño:
                print("")
                print(apuntador.fila,apuntador.columna,end="→")
                i=0
            else:    
                print(apuntador.fila,apuntador.columna, end="→")
            apuntador = apuntador.siguiente


    def actualizar_celdas(self,fila,columna,elemento):
        apuntador=self.root
        while apuntador is not None:
            if apuntador.fila==fila and apuntador.columna==columna:
                apuntador.elemento=elemento
            apuntador=apuntador.siguiente


    def setear_enfermas(self,rejillas):
        for contagiada in rejillas:
            apuntador=self.root
            while apuntador is not None:
                if apuntador.fila==int(contagiada.attrib['f']) and apuntador.columna==int(contagiada.attrib['c']):
                    apuntador.elemento=1
                apuntador=apuntador.siguiente

    def obtener_celda(self,fila,columna):
        apuntador=self.root
        while apuntador is not None:
            if apuntador.fila==fila and apuntador.columna==columna:
                return apuntador
            apuntador=apuntador.siguiente

    def actualizar_enfermas(self,tamaño):
        mtatrix_nueva=Matriz()
        for i in range(tamaño):
            for j in range(tamaño):
                mtatrix_nueva.append(0,i,j)
        apuntador=self.root
        
        while apuntador is not None:
            arriba=self.obtener_celda(apuntador.fila-1,apuntador.columna)
            diag_arr_iz=self.obtener_celda(apuntador.fila-1,apuntador.columna-1)
            diag_arr_der=self.obtener_celda(apuntador.fila-1,apuntador.columna+1)
            izquierda=self.obtener_celda(apuntador.fila,apuntador.columna-1)
            derecha=self.obtener_celda(apuntador.fila,apuntador.columna+1)
            abajo=self.obtener_celda(apuntador.fila+1,apuntador.columna)
            diag_abj_izq=self.obtener_celda(apuntador.fila+1,apuntador.columna-1)
            diag_abj_der=self.obtener_celda(apuntador.fila+1,apuntador.columna+1)
            if arriba!=None and diag_arr_iz!=None and diag_arr_der!=None and izquierda!=None and derecha!=None and abajo!=None and diag_abj_izq !=None and diag_abj_der!=None:

                a=arriba.elemento,diag_arr_iz.elemento,diag_arr_der.elemento,izquierda.elemento,derecha.elemento,abajo.elemento,diag_abj_izq.elemento,diag_abj_der.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#sigue contagiada
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)

            elif arriba==None and izquierda==None and diag_arr_iz==None and diag_arr_der==None and diag_abj_izq==None:# esquina superior izquierda
                
                a=abajo.elemento,diag_abj_der.elemento,derecha.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#sigue contagiada
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)                        
  

            elif arriba==None and derecha==None and diag_arr_iz==None and diag_arr_der==None and diag_abj_der==None:#esquina sup derecha

                a=abajo.elemento,diag_abj_izq.elemento,izquierda.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#contagia
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)                        
 
            elif abajo==None and diag_abj_izq==None and diag_abj_der==None and izquierda==None and diag_arr_iz==None:#esquina inferior izquierda
                a=arriba.elemento,diag_arr_der.elemento,derecha.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)       

            elif abajo==None and diag_abj_izq==None and diag_abj_der==None and derecha==None and diag_arr_der==None:#esquina inferior derecha
                a=arriba.elemento,diag_arr_iz.elemento,izquierda.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)

            elif arriba==None and diag_arr_iz==None and diag_arr_der==None:#fila 0
                a=izquierda.elemento,derecha.elemento,abajo.elemento,diag_abj_izq.elemento,diag_abj_der.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)  

            elif abajo==None and diag_abj_der==None and diag_abj_izq==None:#fila final
                a=izquierda.elemento,derecha.elemento,arriba.elemento,diag_arr_iz.elemento,diag_arr_der.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0) 

            elif izquierda==None and diag_arr_iz==None and diag_abj_izq==None:#columna 0
                a=arriba.elemento,diag_arr_der.elemento,diag_abj_der.elemento,derecha.elemento,abajo.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)

                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)
            elif derecha==None and diag_arr_der==None and diag_abj_der ==None:#columna final
                a=arriba.elemento,diag_arr_iz.elemento,izquierda.elemento,diag_abj_izq.elemento,abajo.elemento
                if apuntador.elemento==0:#celula sana
                    if a.count(1)==3:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                else:#celula enferma 
                    if a.count(1)==2 or a.count(1)==3:#se sana
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,1)
                    else:
                        mtatrix_nueva.actualizar_celdas(apuntador.fila,apuntador.columna,0)

            apuntador=apuntador.siguiente

        return mtatrix_nueva


        
        
           


            

