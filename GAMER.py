import ESTUDIANTE as Estudiante


class Gamer(Estudiante.Estudiante):

    pass

    def __init__(self):
        self.Nickname_1 = None
        self.Nickname_2 = None
        self.Accion = None
        self.Horas_acc = 0
        self.Aventura = None
        self.Horas_av = 0
        self.Arcade = None
        self.Horas_arc = 0
        self.Deportivo = None
        self.Horas_dep = 0
        self.Estrategia = None
        self.Horas_est = 0
        self.Simulacion = None
        self.Horas_sim = 0
        self.RPG = None
        self.Horas_rpg = 0

# definición de geters para la clase gamers

    def get_nickname_1(self):
        return self.Nickname_1

    def get_nickname_2(self):
        return self.Nickname_2

    def get_accion(self):
        return self.Accion

    def get_h_acc(self):
        return self.Horas_acc

    def get_aventura(self):
        return self.Aventura

    def get_h_aventura(self):
        return self.Horas_av

    def get_arcade(self):
        return self.Arcade

    def get_h_arc(self):
        return self.Horas_arc

    def get_deportes(self):
        return self.Deportivo

    def get_h_dep(self):
        return self.Horas_dep

    def get_estrategia(self):
        return self.Estrategia

    def get_h_est(self):
        return self.Horas_est

    def get_simulacion(self):
        return self.Simulacion

    def get_h_sim(self):
        return self.Horas_sim

    def get_rpg(self):
        return self.RPG

    def get_h_rpg(self):
        return self.RPG

# definición de seters para la clase gamer

    def set_id_gamer(self, id_g):
        self.ID = id_g

    def set_nickname_1(self):
        self.Nickname_1 = input('Ingresa tu gamer tag: ')

    def set_nickname_2(self):
        self.Nickname_2 = input('Ingresa tu gamer tag de respaldo: ')

    def set_accion(self):
        self.Accion = int(input('Si te gustanlos juegos de accíon, shooters y peleas freneticas pon uno(1) de lo contrario cero(0): '))

    def set_h_acc(self):
        self.Horas_acc = int(input('¿Cuantas horas de juego tienes?: '))

    def set_aventura(self):
        self.Aventura = int(input('Si te gustanlos juegos de aventura, exploración y mundos abiertos pon uno(1) de lo contrario cero(0): '))

    def set_h_av(self):
        self.Horas_av = int(input('¿Cuantas horas de juego tienes?: '))

    def set_arcade(self):
        self.Arcade = int(input('Si te gustanlos juegos de plataformas con mecanicas complejas y acertijos pon uno(1) de lo contrario cero(0): '))

    def set_h_arc(self):
        self.Horas_arc = int(input('¿Cuantas horas de juego tienes?: '))

    def set_deportes(self):
        self.Deportivo = int(input('Si te gustanlos juegos de deportes pon uno(1) de lo contrario cero(0): '))

    def set_h_dep(self):
        self.Horas_dep = int(input('¿Cuantas horas de juego tienes?: '))

    def set_estrategia(self):
        self.Estrategia = int(input('Si te gustanlos juegos de estrategía y planeación pon uno(1) de lo contrario cero(0): '))

    def set_h_est(self):
        self.Horas_est = int(input('¿Cuantas horas de juego tienes?: '))

    def set_simulacion(self):
        self.Simulacion = int(input('Si te gustanlos juegos de simulacíon y VR pon uno(1) de lo contrario cero(0): '))

    def set_h_sim(self):
        self.Horas_sim = int(input('¿Cuantas horas de juego tienes?: '))

    def set_rpg(self):
        self.RPG = int(input('Si te gustanlos juegos de rol y mundos fantasticos pon uno(1) de lo contrario cero(0): '))

    def set_h_rpg(self):
        self.Horas_rpg = int(input('¿Cuantas horas de juego tienes?: '))

    def datos_gamer(self):
        datos_g = (self.ID, self.Nickname_1, self.Nickname_2, self.Accion, self.Horas_acc, self.Aventura, self.Horas_av, self.Arcade, self.Horas_arc, self.Deportivo, self.Horas_dep, self.Estrategia, self.Horas_est, self.Simulacion, self.Horas_sim, self.RPG, self.Horas_rpg)
        return datos_g

