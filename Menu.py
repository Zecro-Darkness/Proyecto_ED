
from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (grid). Ventana dimensionable

class Aplicacion():
    def __init__(self):
        






        self.raiz = Tk()
        self.raiz.title("Tu amigo UN")
        fuente = font.Font(weight='bold')
        self.raiz.iconbitmap("unal.ico")  
        self.marco = ttk.Frame(self.raiz, borderwidth=8,
                               relief="raised", padding=(400,300))
        self.etiq1 = ttk.Label(self.marco, text="ID:", 
                               font=fuente, padding=(5,5))
        self.etiq2 = ttk.Label(self.marco, text="Nombre:", 
                               font=fuente, padding=(5,5))
        self.etiq3 = ttk.Label(self.marco, text="Apellido:", 
                               font=fuente, padding=(5,5))
        self.etiq4 = ttk.Label(self.marco, text="Edad:", 
                               font=fuente, padding=(5,5))
        self.etiq5 = ttk.Label(self.marco, text="Correo institucional:", 
                             font=fuente, padding=(5,5))
        self.etiq6 = ttk.Label(self.marco, text="Ciudad de origen:", 
                               font=fuente, padding=(5,5))
        self.etiq7 = ttk.Label(self.marco, text="Gamer(Si o No):", 
                               font=fuente, padding=(5,5))
        self.etiq8 = ttk.Label(self.marco, text="Series_tv(Si o No):", 
                               font=fuente, padding=(5,5))

        self.id = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.edad = StringVar()
        self.correo = StringVar()
        self.ciudad = StringVar()
        self.gamer = StringVar()
        self.series = StringVar()
        self.id.set(getpass.getuser())        
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.id,
                                width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.nombre,
                                width=30)
        self.ctext3 = ttk.Entry(self.marco, textvariable=self.apellido,
                                width=30)
        self.ctext4 = ttk.Entry(self.marco, textvariable=self.edad,
                                width=30)
        self.ctext5 = ttk.Entry(self.marco, textvariable=self.correo,
                                width=30)
        self.ctext6 = ttk.Entry(self.marco, textvariable=self.ciudad,
                                width=30)
        self.ctext7 = ttk.Entry(self.marco, textvariable=self.gamer,
                                width=30)
        self.ctext8 = ttk.Entry(self.marco, textvariable=self.series,
                                width=30)

        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Aceptar", 
                                 padding=(5,5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text="Cancelar", 
                                 padding=(5,5), command=quit)
        self.unal=PhotoImage(file="Unal.png")
        self.image = ttk.Label(self.marco, image=self.unal, padding=(1,1))


        # Para conseguir que la cuadricula y los widgets se 
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el 
        # widget dentro de su celda, cuando se modifique la 
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará 
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño. 
        # Pero con definir la opción 'sticky' no es suficiente: 
        # hay activar esta propiedad más adelante.
        
        self.image.place(x=-400, y=-300) 
        self.marco.grid(column=0, row=0, padx=40, pady=40, 
                        sticky=(N, S, E, W))
        self.etiq1.grid(column=0, row=0, 
                        sticky=(N, S, E, W))
        self.ctext1.grid(column=1, row=0, columnspan=2, 
                         sticky=(E, W))
        self.etiq2.grid(column=0, row=1,
                        sticky=(N, S, E, W))
        self.ctext2.grid(column=1, row=1, columnspan=2, 
                         sticky=(E, W))
        self.etiq3.grid(column=0, row=2,
                        sticky=(N, S, E, W))
        self.ctext3.grid(column=1, row=2, columnspan=3, 
                         sticky=(E, W))
        self.etiq4.grid(column=0, row=3,
                        sticky=(N, S, E, W))
        self.ctext4.grid(column=1, row=3, columnspan=3, 
                         sticky=(E, W))
        self.etiq5.grid(column=0, row=4,
                        sticky=(N, S, E, W))
        self.ctext5.grid(column=1, row=4, columnspan=2, 
                         sticky=(E, W))
        self.etiq6.grid(column=0, row=5,
                        sticky=(N, S, E, W))
        self.ctext6.grid(column=1, row=5, columnspan=2, 
                         sticky=(E, W))
        self.etiq7.grid(column=0, row=6,
                        sticky=(N, S, E, W))
        self.ctext7.grid(column=1, row=6, columnspan=2, 
                         sticky=(E, W))
        self.etiq8.grid(column=0, row=7,
                        sticky=(N, S, E, W))
        self.ctext8.grid(column=1, row=7, columnspan=2, 
                         sticky=(E, W))
        self.separ1.grid(column=0, row=8, columnspan=3, pady=5, 
                         sticky=(N, S, E, W))
        self.boton1.grid(column=1, row=9, padx=5, 
                         sticky=(E))
        self.boton2.grid(column=2, row=9, padx=5, 
                         sticky=(W))

        # A continuación, se activa la propiedad de expandirse
        # o contraerse definida antes con la opción
        # 'sticky' del método grid().
        # La activación se hace por contenedores y por filas
        # y columnas asignando un peso a la opción 'weight'.
        # Esta opción asigna un peso (relativo) que se utiliza
        # para distribuir el espacio adicional entre columnas
        # y/o filas. Cuando se expanda la ventana, una columna
        # o fila con un peso 2 crecerá dos veces más rápido
        # que una columna (o fila) con peso 1. El valor
        # predeterminado es 0 que significa que la columna o
        # o fila no crecerá nada en absoluto. 
        # Lo habitual es asignar pesos a filas o columnas donde 
        # hay celdas con widgets.

        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(0, weight=1)
        self.marco.columnconfigure(0, weight=1)
        self.marco.columnconfigure(1, weight=1)
        self.marco.columnconfigure(2, weight=1)
        self.marco.rowconfigure(0, weight=1)
        self.marco.rowconfigure(1, weight=1)
        self.marco.rowconfigure(4, weight=1)
        
        # Establece el foco en la caja de entrada de la
        # contraseña.
        
        self.ctext2.focus_set()
        self.raiz.mainloop()
    
    def aceptar(self):
        if self.nombre.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.ctext1.get())
            print("Contraseña:", self.ctext2.get())
        else:
            print("Acceso denegado")
            self.nombre.set("")
            self.ctext2.focus_set()

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()