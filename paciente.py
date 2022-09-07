class paciente:
    def __init__(self,nombre,edad,periodos,m,contagiadas):
        self.nombre=nombre
        self.edad=edad
        self.periodos=periodos
        self.m=m
        self.contagiadas=contagiadas

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad    

    def get_periodos(self):
        return self.periodos

    def get_m(self):
        return self.m

    def get_contagiadas(self):
        return self.contagiadas

    def set_nombre(self,nombre):
        self.nombre=nombre            


    def set_edad(self,edad):
        self.edad=edad

    def set_periodos(self,periodos):
        self.periodos=periodos        

    def set_m(self,m):
        self.m=m

    def set_contagiadas(self,contagiadas):
        self.contagiadas=contagiadas

    def obtener_rejillas_contagiadas(self):
        for rejilla in self.contagiadas:
            print(rejilla.attrib)
                    


