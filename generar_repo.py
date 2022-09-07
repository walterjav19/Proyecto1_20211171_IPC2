class repo:

    def __init__(self,nombre,edad,periodo,m,resultado):
        self.nombre=nombre
        self.edad=edad
        self.periodo=periodo
        self.m=m
        self.resultado=resultado
        

    def cuerpo(self):
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

    def crear_xml(self):
        cabecera = "<?xml version='1.0' encoding='UTF-8'?>\n<pacientes>\n"
        file = open("diagnostico.xml","w")
        file.write(cabecera+self.cuerpo())
        file.close()

