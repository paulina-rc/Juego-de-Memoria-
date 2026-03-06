from kivy.app import App #libreria de Kivy 
from kivy.uix.gridlayout import GridLayout #libreria de Kivy 
from kivy.uix.button import Button #libreria de Kivy 
from kivy.uix.label import Label #para mostrar texto
from kivy.uix.popup import Popup #para mostrar ventana de tiempos
from kivy.clock import Clock #libreria para temporizadores
from kivy.uix.textinput import TextInput #para ingresar nombre de jugadores
from datetime import datetime #para guardar fecha
import random


class JuegoMemoria(GridLayout):

    def __init__(self, **kwargs): #esta función se ejecuta automáticamente cuando se crea el objeto
                                    #ejemplo: tablero = juego de memoria 
        super().__init__(**kwargs) #"Kwargs" son parametros que se ponen por default

        self.cols = 4 #asigna 4 columnas al tablero 
        
        self.cartas_seleccionadas = [] #lista donde se guardan todas las cartas abiertas 

        self.movimientos = 0 #cantidad de movimientos del jugador 

        self.pares_encontrados = 0 #contador de pares encontrados 

        self.tiempo = 0 #contador de tiempo 

        self.jugador1 = "" #variable para nombre del jugador 
        self.jugador2 = "" #

        self.turno = 1 #indicador de jugador de cada jugador

        self.puntos_j1 = 0 #puntaje de jugadores 
        self.puntos_j2 = 0

        self.modo_multijugador = False #variable para saber si el juego es multijugador



                                    #SECCION DE DISEÑO 

        # titulo del juego 
        self.titulo = Label(text="JUEGO DE MEMORIA", size_hint=(1,0.1))
        self.add_widget(self.titulo)

        # muestra timpo de pantalla 
        self.label_tiempo = Label(text="Tiempo: 0", size_hint=(1,0.1))
        self.add_widget(self.label_tiempo)

        # label que muestra movimientos
        self.label_movimientos = Label(text="Movimientos: 0", size_hint=(1,0.1))
        self.add_widget(self.label_movimientos)

        # label que indica turno del jugador
        self.label_turno = Label(text="Turno: ", size_hint=(1,0.1))
        self.add_widget(self.label_turno)

        # label que muestra puntos
        self.label_puntos = Label(text="Puntos", size_hint=(1,0.1))
        self.add_widget(self.label_puntos)

        # boton para ver historial de tiempos
        self.boton_historial = Button(text="Ver tiempos guardados", size_hint=(1,0.1))
        self.boton_historial.bind(on_press=self.ver_tiempos)
        self.add_widget(self.boton_historial)

        # iniciar temporizador
        Clock.schedule_interval(self.actualizar_tiempo, 1)

        # seccion de imagenes de los botones 
        self.imagenes = [ #arreglo con imagenes 
            "img/Beso.jpg",
            "img/Brillo.png",
            "img/Cereza.png",
            "img/Corona.png",
            "img/Diamante.jpg",
            "img/Estrella.png",
            "img/Flores.jpg",
            "img/Mono.png",
        ] * 2 #multiplica las imagens por dos para poder hacer pares 

        random.shuffle(self.imagenes) #rando.shuffle organiza las cartas random, las remuerve 

        for imagen in self.imagenes: #recorre todas las imagenes de la lista 

            boton = Button( #crador del boton 
                background_normal="img/Pregunta.jpg", # imagen cuando no se preciona 
                background_down="img/Pregunta.jpg" # imagen cuando se preciona 
            )

            # super IMPORTANTE guardamos el valor del boton en este caso la imagen
            boton.imagen_real = imagen

            boton.bind(on_press=self.cambiar_imagen) #cuando se precione se va a ejecutar la funcion que se especifica
            self.add_widget(boton) #agregar carta al tablero 


        # --------------------------------
        # ELEGIR MODO DE JUEGO
        # --------------------------------

        Clock.schedule_once(self.elegir_modo,1)


    # ventana para elegir modo de juego (solitario o multijugador)
    def elegir_modo(self, dt):

        layout = GridLayout(cols=1)

        boton_solo = Button(text="Modo Solitario")
        boton_multi = Button(text="Modo Multijugador")

        boton_solo.bind(on_press=self.modo_solitario)
        boton_multi.bind(on_press=self.modo_multijugador_func)

        layout.add_widget(boton_solo)
        layout.add_widget(boton_multi)

        self.popup_modo = Popup(
            title="Selecciona modo de juego",
            content=layout,
            size_hint=(0.6,0.6)
        )

        self.popup_modo.open()


    # modo solitario
    def modo_solitario(self, boton):

        self.modo_multijugador = False

        self.label_turno.text = "Modo: Solitario"
        self.label_puntos.text = ""

        self.popup_modo.dismiss()


    # modo multijugador
    def modo_multijugador_func(self, boton):

        self.modo_multijugador = True

        self.popup_modo.dismiss()

        self.pedir_nombres(0)


    # ventana para ingresar nombres de jugadores
    def pedir_nombres(self, dt):

        layout = GridLayout(cols=1)

        self.input_j1 = TextInput(hint_text="Nombre Jugador 1")
        self.input_j2 = TextInput(hint_text="Nombre Jugador 2")

        boton = Button(text="Comenzar")
        boton.bind(on_press=self.iniciar_juego)

        layout.add_widget(self.input_j1)
        layout.add_widget(self.input_j2)
        layout.add_widget(boton)

        self.popup = Popup(
            title="Ingrese nombres de jugadores",
            content=layout,
            size_hint=(0.7,0.7)
        )

        self.popup.open()


    def iniciar_juego(self, boton): #guardar nombres de jugadores 

        self.jugador1 = self.input_j1.text #input para nombres de jugadores 
        self.jugador2 = self.input_j2.text #input para nombres de jugadores 

        if self.jugador1 == "":
            self.jugador1 = "Jugador 1"

        if self.jugador2 == "":
            self.jugador2 = "Jugador 2"

        # mostrar turno inicial
        self.label_turno.text = "Turno: " + self.jugador1

        # mostrar puntos iniciales
        self.label_puntos.text = self.jugador1 + ": 0 | " + self.jugador2 + ": 0"

        self.popup.dismiss()


    def actualizar_tiempo(self, dt):

        # aumentar tiempo cada segundo
        self.tiempo += 1
        self.label_tiempo.text = "Tiempo: " + str(self.tiempo)


    def cambiar_imagen(self, boton):

        # evitar que se presione la misma carta dos veces
        if boton in self.cartas_seleccionadas:
            return

        # mostrar imagen real
        boton.background_normal = boton.imagen_real
        boton.background_down = boton.imagen_real

        # guardar carta seleccionada
        self.cartas_seleccionadas.append(boton)

        # si hay 2 cartas abiertas
        if len(self.cartas_seleccionadas) == 2:

            # sumar movimiento (destapar dos cartas cuenta como 1)
            self.movimientos += 1
            self.label_movimientos.text = "Movimientos: " + str(self.movimientos)

            # esperar 1 segundo antes de comparar
            Clock.schedule_once(self.comparar_cartas, 1)


    def comparar_cartas(self, dt):

        carta1 = self.cartas_seleccionadas[0]
        carta2 = self.cartas_seleccionadas[1]

        if carta1.imagen_real != carta2.imagen_real:

            # si no coinciden se vuelven a ocultar
            carta1.background_normal = "img/Pregunta.jpg"
            carta1.background_down = "img/Pregunta.jpg"

            carta2.background_normal = "img/Pregunta.jpg"
            carta2.background_down = "img/Pregunta.jpg"

            # cambiar turno SOLO si es multijugador
            if self.modo_multijugador:

                if self.turno == 1:
                    self.turno = 2
                    self.label_turno.text = "Turno: " + self.jugador2
                else:
                    self.turno = 1
                    self.label_turno.text = "Turno: " + self.jugador1

        else:
            # si coinciden aumentamos pares encontrados
            self.pares_encontrados += 1

            # sumar punto al jugador actual solo en multijugador
            if self.modo_multijugador:

                if self.turno == 1:
                    self.puntos_j1 += 1
                else:
                    self.puntos_j2 += 1

                self.label_puntos.text = self.jugador1 + ": " + str(self.puntos_j1) + " | " + self.jugador2 + ": " + str(self.puntos_j2)

        # limpiar lista
        self.cartas_seleccionadas = []

        # verificar si el juego terminó
        if self.pares_encontrados == 8:

            # detener el temporizador
            Clock.unschedule(self.actualizar_tiempo)

            # guardar tiempo
            self.guardar_tiempo()

            # determinar ganador
            if self.puntos_j1 > self.puntos_j2:
                ganador = self.jugador1
            elif self.puntos_j2 > self.puntos_j1:
                ganador = self.jugador2
            else:
                ganador = "Empate"

            # mostrar ventana de victoria
            mensaje = "Ganador: " + ganador + "\nTiempo: " + str(self.tiempo) + " segundos"

            popup = Popup(
                title="Fin del juego",
                content=Label(text=mensaje),
                size_hint=(0.6,0.6)
            )

            popup.open()


    def guardar_tiempo(self):

        archivo = open("tiempos.txt", "a")
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        texto = "Fecha: " + fecha + " Tiempo: " + str(self.tiempo) + " segundos\n"
        archivo.write(texto)
        archivo.close()


    def ver_tiempos(self, boton):

        try:
            archivo = open("tiempos.txt", "r")
            contenido = archivo.read()
            archivo.close()
        except:
            contenido = "No hay tiempos guardados"

        popup = Popup(
            title="Tiempos guardados",
            content=Label(text=contenido),
            size_hint=(0.8,0.8)
        )

        popup.open()


class JuegoApp(App):
    def build(self):
        return JuegoMemoria()


if __name__ == "__main__":
    JuegoApp().run()

    