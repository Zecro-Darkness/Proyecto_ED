import sqlite3
from sqlite3 import Error
import LINKED_LIST as l_list
import GAMER as gamer_c
import ESTUDIANTE as estudiante_c
import SERIES as estudiante_s
import time

# Crea la conexíon a la base de datos en caso de fallar imprimirá 'error'


def conexion_a_la_db():
    try:
        con = sqlite3.connect('BD_TuAmigoUN.db')
        return con
    except Error:
        print(Error)


def cerrar_bd(con):
    con.close()

# metodo para ingresar los datos del usuario en la tabla de usuarios principal, usa sentecias sql
# hay que tener en cuenta que depues del insert into se debe colocar el nombre de la tabla de destino,
# y los interrogantes es la cantidad de valores que pide la tabla y la ultima variable es una tupla de string y enteros
# con los datos a ingresar en la tabla esta última es muy importante


def ingresar_usuario(con, d_usuario):
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO Usuarios VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', d_usuario)
    con.commit()
    return True


def ingresar_gamer(con, d_gamer):
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO Gamers VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', d_gamer)
    con.commit()
    return True


def ingresar_series(con, d_series):
    cursor_obj = con.cursor()
    cursor_obj.execute('''INSERT INTO Series VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', d_series)
    con.commit()
    return True


def consulta_general(con):

    cursor_obj = con.cursor()

    consulta = "SELECT * FROM Usuarios"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        inicio = time.time()
        for i in range(0, 8):

            dato = row[i]
            cleinte_ind.append(dato)

        todos.append(str(cleinte_ind))
        fin = time.time()
        cleinte_ind.limpiar()
        cont += 1


    print(str(todos))

    print(' Amigos encontrados: ' + str(cont))
    print(' tiempo de ejecución: ', fin - inicio)

def consulta_gamers(con):
    cursor_obj = con.cursor()

    consulta = "SELECT * FROM Usuarios WHERE Juegos == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        for i in range(0, 8):
            cleinte_ind.append(row[i])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))

def cons_g_acc(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Accion == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0
    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_g_avt(con):
    cursor_obj = con.cursor()
    cursor_obj_2 =con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Aventura == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_g_arc(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Arcade == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])

        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_g_dep(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Deportivos == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_g_est(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Estrategia == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos Encontrados: ' + str(cont))


def cons_g_sim(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE Simulación == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_g_rpg(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Gamers WHERE RPG == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def consulta_series(con):
    cursor_obj = con.cursor()

    consulta = "SELECT * FROM Usuarios WHERE Series == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        for i in range(0, 8):
            cleinte_ind.append(row[i])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_s_a_c(con):

    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Animadas == 1 and Cartoons == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_s_a_a(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Animadas == 1 and Anime == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_s_a(con):
    cursor_obj = con.cursor()
    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Animadas == 1 "

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_s_d(con):

    cursor_obj = con.cursor()

    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Doramas == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_s_doc(con):

    cursor_obj = con.cursor()

    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Documentales == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_s_n(con):

    cursor_obj = con.cursor()

    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE USA_Norm == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def cons_s_nov(con):

    cursor_obj = con.cursor()

    cursor_obj_2 = con.cursor()

    consulta = "SELECT Identificador FROM Series WHERE Novelas == 1"

    cursor_obj.execute(consulta)

    filas = cursor_obj.fetchall()

    cleinte_ind = l_list.LinkedList()

    todos = l_list.LinkedList()

    cont = 0

    for row in filas:
        ident = str(row[0])
        cons = 'SELECT Nombres, Apellidos, Edad, E_mail, Ciudad FROM Usuarios WHERE Identificador == "' + ident + '"'
        cursor_obj_2.execute(cons)
        espacios = cursor_obj_2.fetchall()
        for col in espacios:
            for j in range(0, 5):
                cleinte_ind.append(col[j])
        todos.append(str(cleinte_ind))
        cleinte_ind.limpiar()
        cont += 1
    print(str(todos))
    print(' Amigos encontrados: ' + str(cont))


def menu(con):
    salir = False
    while not salir:
        estudiante = estudiante_c.Estudiante()
        opc = int(input('''Bienvenido a Tu Amigo UN

                     Seleciona el número de la opción que deseas elegir.
                     
                     1) Dejar mi huella.
                     
                     2) Buscar amigos
                     
                     3) Salir
                     
                     >>> '''))
        if opc == 1:
            estudiante.set_id()
            estudiante.set_f_name()
            estudiante.set_l_name()
            estudiante.set_edad()
            estudiante.set_e_mail()
            estudiante.set_city()
            estudiante.set_gamer()

            # comprobación de suscripción a gamers en caso de si se piden datos de preferencias

            if estudiante.get_gamer() == 1:
                gamer = gamer_c.Gamer()
                id_gm = estudiante.get_id()
                gamer.set_id_gamer(id_gm)
                gamer.set_accion()
                gamer.set_aventura()
                gamer.set_arcade()
                gamer.set_deportes()
                gamer.set_estrategia()
                gamer.set_simulacion()
                gamer.set_rpg()
                datos_g = gamer.datos_gamer()
                ingresar_gamer(con, datos_g)
            estudiante.set_series()

            # comprobación de suscripción a series en caso de si se piden datos de preferencias

            if estudiante.get_series() == 1:
                series = estudiante_s.Series()
                id_ser = estudiante.get_id()
                series.set_id_series(id_ser)
                series.set_animadas()
                series.set_cartoons()
                series.set_animes()
                series.set_doramas()
                series.set_documentales()
                series.set_series_normales()
                series.set_novelas()
                datos_s = series.datos_series()
                ingresar_series(con, datos_s)

            datos_e = estudiante.datos()
            ingresar_usuario(con, datos_e)
            print('Ingreso satisfactorio')

        elif opc == 2:
            while not salir:
                seleccion = int(input("""Encuentra tu parche (seleciona el número de la opción que quieres elegir):
                                        1) Todos
                                        
                                        2) Gamers
                                        
                                        3) Serie-aficionados
                                        
                                        4) Regresar
                                        
                                        >>>"""))
                if seleccion == 1:
                    consulta_general(con)
                elif seleccion == 2:
                    while not salir:
                        gamer_opc = int(input("""¿Que clase de team quieres?(seleciona el número de la opción que quieres elegir):

                                                             1) Todos: Encuentra tu team o duo entre toda la comunidad Gamer de la U

                                                             2) Acción: Encuentra tu team o duo entre los amantes de los juegos de acción disparos y combate

                                                             3) Aventureros: Encuentra tu team o duo entre los amantes de ka avebtura y la exploración

                                                             4) Arcadieros: Encuentra tu team o duo entre los amantes de juegos freneticos y puzles

                                                             5) Deportes: Encuentra tu team o duo entre los amantes de los juegos deportivos

                                                             6) Estrategas:Encuentra tu team o duo entre los amantes de los juegos de estrategia y corrdinación

                                                             7) Simuladores: Encuentra tu team o duo entre los amantes de los simuladores y juegos VR

                                                             8) RPG´s: Encuentra tu team o duo entre los amantes de juegos de rol e historisa fantasticas

                                                             9) Regresar

                                                             >>>"""))
                        if gamer_opc == 1:
                            consulta_gamers(con)

                        elif gamer_opc == 2:
                            cons_g_acc(con)

                        elif gamer_opc == 3:
                            cons_g_avt(con)

                        elif gamer_opc == 4:
                            cons_g_arc(con)

                        elif gamer_opc == 5:
                            cons_g_dep(con)

                        elif gamer_opc == 6:
                            cons_g_est(con)

                        elif gamer_opc == 7:
                            cons_g_sim(con)

                        elif gamer_opc == 8:
                            cons_g_rpg(con)

                        elif gamer_opc == 9:
                            break
                elif seleccion == 3:
                    while not salir:
                        series_s = int(input("""¿Con quien quieres ver series?: 

                                                1) Todos: Encuentra amigos con diferentes tipos de gustos

                                                2) Animadas: Encuentra aficionados por todo tipo de series animadas

                                                3) Doramas: Encuentra aficionados a los dramas Koreanos

                                                4) Documentales: Encuentra aficionados a los documentales y las series del mundo real

                                                5) Series: Encuentra aficionados de series clasicas americanas y latinas

                                                6) Novelas: Encuentra aficionados a las novelas e historias romanticas

                                                7) Regresar
                                                
                                                >>>"""))
                        if series_s == 1:
                            consulta_series(con)
                        elif series_s == 2:
                            while not salir:
                                series_a = int(input("""¿Que series animadas prefieres?
                                                        1) Cartoon
                                                    
                                                        2)Anime
                                                    
                                                        3)Todas
                                                        
                                                        4)Regresar
                                                        
                                                        >>>"""))
                                if series_a == 1:
                                    cons_s_a_c(con)
                                elif series_a == 2:
                                    cons_s_a_a(con)
                                elif series_a == 3:
                                    cons_s_a(con)
                                elif series_a == 4:
                                    break
                        elif series_s == 3:
                            cons_s_d(con)
                        elif series_s == 4:
                            cons_s_doc(con)
                        elif series_s == 5:
                            cons_s_n(con)
                        elif series_s ==6:
                            cons_s_nov(con)
                        elif series_s == 7:
                            break

                elif seleccion == 4:
                    break
        elif opc == 3:



            break


def main():
    con = conexion_a_la_db()
    menu(con)
    cerrar_bd(con)

main()
