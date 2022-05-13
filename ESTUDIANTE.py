"""Una de las clases principales para el funcionamiento del programa, se definen atributos principales y para el guardado
en la base de datos se usa como PK el ID o cedula, támbien en un futuro se usará para hacecr login, solo se definen setters
y getters ya que la función principal de esta clase es capturar los datos del usuario para introducirlos a la BD"""

class Estudiante:
    def __int__(self):
        self.ID = None
        self.F_Name = None
        self.L_Name = None
        self.Edad = None
        self.E_mail = None
        self.City = None
        self.Gamer = None
        self.Series_tv = None


    def get_id(self):
        return self.ID

    def get_f_name(self):
        return self.F_Name

    def get_l_name(self):
        return self.L_Name

    def get_edad(self):
        return self.Edad

    def get_e_mail(self):
        return self.E_mail

    def get_city(self):
        return self.City

    def get_gamer(self):
        return self.Gamer

    def get_series(self):
        return self.Series_tv

    def set_id(self):
        self.ID = input('Identificación: ')
        self.ID = self.ID.ljust(12)

    def set_f_name(self):
        self.F_Name = input('Nombres: ')

    def set_l_name(self):
        self.L_Name = input('Apellidos: ')

    def set_edad(self):
        self.Edad = int(input('Edad: '))

    def set_e_mail(self):
        self.E_mail = input('Correo Institucional: ')

    def set_city(self):
        self.City = input('Ciudad de Origen : ')

    def set_gamer(self):
        self.Gamer = int(input('¿Te gustan los videojuegos?(1 para si 0 para no): '))

    def set_series(self):
        self.Series_tv = int(input('¿Te gustan las Series?(1 para si 0 para no): )'))

"""el metodo datos ayuda a recopilar la información del objeto estudiante para multiples usos, desde registro
hasta busqueda, este metodo retorma una tupla de strings y enteros para ingresar a la BD o consultar."""
    
    def datos(self):
        datos = (self.ID, self.F_Name, self.L_Name, self.Edad, self.E_mail, self.City, self.Gamer, self.Series_tv)
        return datos
    
    
    
