class repo:

    def __init__(self,nombre,edad,periodo,m,resultado,n1):
        self.nombre=nombre
        self.edad=edad
        self.periodo=periodo
        self.m=m
        self.resultado=resultado
        self.n1=n1
        

    def cuerpo_grave(self):
        cuerpo=""
        cuerpo='''  <paciente>
        <datospersonales>
            <nombre>'''+self.nombre+'''</nombre>
            <edad>'''+str(self.edad)+'''</edad>
        </datospersonales>
        <periodos>'''+str(self.periodo)+'''</periodos>
        <m>'''+str(self.m)+'''</m>
        <resultado>'''+self.resultado+'''</resultado>
    </paciente>'''

        return cuerpo


    def cuerpo_mortal(self):
        cuerpo2=""
        cuerpo2='''  <paciente>
        <datospersonales>
            <nombre>'''+self.nombre+'''</nombre>
            <edad>'''+str(self.edad)+'''</edad>
        </datospersonales>
        <periodos>'''+str(self.periodo)+'''</periodos>
        <m>'''+str(self.m)+'''</m>
        <resultado>'''+self.resultado+'''</resultado>
            <n1>'''+self.n1+'''<n1/>
    </paciente>'''

        return cuerpo2

    
    def crear_xml_grave(self):
        cabecera = "<?xml version='1.0' encoding='UTF-8'?>\n<pacientes>\n"
        file = open("diagnostico_grave.xml","w")
        file.write(cabecera+self.cuerpo_grave())
        file.close()

    def crear_xml_mortal(self):
        cabecera = "<?xml version='1.0' encoding='UTF-8'?>\n<pacientes>\n"
        file = open("diagnostico_mortal.xml","w")
        file.write(cabecera+self.cuerpo_mortal())
        file.close()


