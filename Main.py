from kivy.app import App #libreria de Kivy 
from kivy.uix.gridlayout import GridLayout #libreria de Kivy 
from kivy.uix.button import Button #libreria de Kivy 
from kivy.uix.label import Label #para mostrar texto
from kivy.uix.popup import Popup #para mostrar ventana de tiempos
from kivy.clock import Clock #libreria para temporizadores
from kivy.uix.textinput import TextInput #para ingresar nombre de jugadores
from datetime import datetime #para guardar fecha
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
Window.clearcolor = (0.12, 0.12, 0.15, 1)


class JuegoMemoria(BoxLayout):

    def __init__(self, **kwargs): #esta función se ejecuta automáticamente cuando se crea el objeto
                                    #ejemplo: tablero = juego de memoria 
        super().__init__(**kwargs) #"Kwargs" son parametros que se ponen por default
        
        self.orientation = "vertical"

        # panel superior del juego
        panel_superior = GridLayout(cols=6, size_hint=(1,0.15))
        self.add_widget(panel_superior)
        # tablero de cartas
        self.tablero = GridLayout(cols=4, spacing=15, padding=20, size_hint=(1,0.85))
        self.add_widget(self.tablero)
        
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


                            #DISENO VISUAL  

       # titulo del juego
        self.titulo = Label(text="JUEGO DE MEMORIA", size_hint=(1,0.1))
        panel_superior.add_widget(self.titulo)

        #muestra el tiempo en pantalla
        self.label_tiempo = Label(text="Tiempo: 0", size_hint=(1,0.1))
        panel_superior.add_widget(self.label_tiempo)

        #muestra de movimientos
        self.label_movimientos = Label(text="Movimientos: 0", size_hint=(1,0.1))
        panel_superior.add_widget(self.label_movimientos)

        #indicador de turno del jugador
        self.label_turno = Label(text="Turno: ", size_hint=(1,0.1))
        panel_superior.add_widget(self.label_turno)

        #contador de puntos
        self.label_puntos = Label(text="Puntos", size_hint=(1,0.1))
        panel_superior.add_widget(self.label_puntos)

        #ver historial de tiempos
        self.boton_historial = Button(text="Ver tiempos guardados", size_hint=(1,0.1))
        self.boton_historial.bind(on_press=self.ver_tiempos)
        panel_superior.add_widget(self.boton_historial)

        Clock.schedule_interval(self.actualizar_tiempo, 1) #iniciar temporizador 

        # SECCION DE IMAGENES DE CARTAS
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

        for imagen in self.imagenes:

            boton = Button(
                background_normal="",
                background_down="",
                size_hint=(1,1)
            )
            
            # super IMPORTANTE guardamos el valor del boton en este caso la imagen
            boton.imagen_real = imagen

            boton.bind(on_press=self.cambiar_imagen)

            # agregar carta al tablero
            self.tablero.add_widget(boton)

        Clock.schedule_once(self.elegir_modo,1) #elegir modo de juego 


    # ventana para elegir modo de juego (solitario o multijugador)
    def elegir_modo(self, dt): #función para elegir modo de juego 

        layout = GridLayout(cols=1)  #crear el layout (contenedor para poner botones)

        boton_solo = Button(text="Modo Solitario") #crear boton para la opcion de modo solitario 
        boton_multi = Button(text="Modo Multijugador") #crear boton para la opcio de multijugador 

        boton_solo.bind(on_press=self.modo_solitario) #conexion de botones con funciones 
        boton_multi.bind(on_press=self.modo_multijugador_func) #conexion de botones con funciones

        layout.add_widget(boton_solo) #agregado de botones al layaout
        layout.add_widget(boton_multi) #agregar botones al layaout 

        self.popup_modo = Popup( #creacion de ventana emerguente 
            title="Selecciona modo de juego", #titulo del popup
            content=layout, #contenido del popup (popput es algo emerguente que aparece encime de toda la pagina o apliacion )
            size_hint=(0.6,0.6) #tamaño del popup
        )                       #0.6 = 60% del ancho de la pantalla
                                #0.6 = 60% de la altura de la pantalla

        self.popup_modo.open() #mostrar la ventana 


    # modo solitario
    def modo_solitario(self, boton): #self, hace referencia al objeto del juego 
                                     #boton representa el boton precionado 

        self.modo_multijugador = False #se cambia la variable de modo_multijugador a "false"

        self.label_turno.text = "Modo: Solitario" #se cambia el texto para mostar que se esta jugando en modo solitario 
        self.label_puntos.text = "" #se borro el texto de label de puntos 

        self.popup_modo.dismiss() #se cierra la ventana emeguente donde el ususario elije el modo de juego 


    # modo multijugador
    def modo_multijugador_func(self, boton): #llamado de funcion 

        self.modo_multijugador = True #indica el modo de juego 

        self.popup_modo.dismiss() #se cierra la ventana emerguente de pregunta 

        self.pedir_nombres(0) #ejecuta la funcion que pide los nombres a los jugadores 


   # ventana para ingresar nombres de jugadores
    def pedir_nombres(self, dt):

        layout = GridLayout(cols=1) #crear layout, es praticamente un contenedor de elementos con filas y columnas 

        self.input_j1 = TextInput(hint_text="Nombre Jugador 1") #ingredar nombre de jugadores 
        self.input_j2 = TextInput(hint_text="Nombre Jugador 2")

        boton = Button(text="Comenzar") #crear boton para comenzar el juego 
        boton.bind(on_press=self.iniciar_juego) #conexion del boton con la funcion 

        layout.add_widget(self.input_j1) #crea un campo para jugador 1
        layout.add_widget(self.input_j2) #campo para jugador 2
        layout.add_widget(boton) #btn de comenzar 

        self.popup = Popup( #crear ventana emerguente 
            title="Ingrese nombres de jugadores", #tutulo 
            content=layout, #indica que el contenido de la ventana sera el layaout
            size_hint=(0.7,0.7) #definicon de tamano real (0.7 significa 70% del ancho y 70% de la altura de la pantalla.)
        )

        self.popup.open() #muestra al ventana, sin esto el popup no apreceria 


    def iniciar_juego(self, boton): #se define la funcion 

        self.jugador1 = self.input_j1.text #input para nombres de jugadores 
        self.jugador2 = self.input_j2.text #input para nombres de jugadores 

        if self.jugador1 == "": #verifica si el campo del jugador esta vacio 
            self.jugador1 = "Jugador 1" #si esta vacio le coloca jugador 1

        if self.jugador2 == "":
            self.jugador2 = "Jugador 2"

        # indica que el primer jugador es el numero 1
        self.label_turno.text = "Turno: " + self.jugador1

        #muestra el marcador inical de cada jugador 
        self.label_puntos.text = self.jugador1 + ": 0 | " + self.jugador2 + ": 0"

        self.popup.dismiss() #cierre de ventana emeguente de nombres 


    def actualizar_tiempo(self, dt):

        # aumentar tiempo cada segundo
        self.tiempo += 1
        self.label_tiempo.text = "Tiempo: " + str(self.tiempo)


    def cambiar_imagen(self, boton): #cada que el jugador preciona un boton/imagen se ejecuta la funcion 

        # evitar que se presione la misma carta dos veces
        if boton in self.cartas_seleccionadas: #revisa si la carta ya fue precionada 
            return

        # mostrar imagen real
        boton.background_normal = boton.imagen_real
        boton.background_down = boton.imagen_real

        # guardar carta seleccionada
        self.cartas_seleccionadas.append(boton)

        # si hay 2 cartas abiertas
        if len(self.cartas_seleccionadas) == 2:

            # sumar movimiento (destapar dos cartas cuenta como 1)
            self.movimientos += 1 #sumatoria de movimientos 
            self.label_movimientos.text = "Movimientos: " + str(self.movimientos)

            # esperar 1 segundo antes de comparar
            Clock.schedule_once(self.comparar_cartas, 1)


    def comparar_cartas(self, dt): #dt es un parámetro que usa Clock cuando la función se ejecuta después de un tiempo

        carta1 = self.cartas_seleccionadas[0] #carta 1 = a primera carta seleccionada 
        carta2 = self.cartas_seleccionadas[1]# carta 2 = a segunda carta seleccionada

        if carta1.imagen_real != carta2.imagen_real: #Si son diferentes, significa que no forman un par

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

        archivo = open("tiempos.txt", "a") #abrimos el archivo (tiempos) la "a" nos permite agregar, esto permite agregar sin borrrar los anteriores 
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M") #se obtiene la fecha y hora actual del sistema
        texto = "Fecha: " + fecha + " Tiempo: " + str(self.tiempo) + " segundos\n" # se crea el texto que se guardara en el archivo 
        archivo.write(texto) #se escribe texto dentro de tiempos.txt
        archivo.close() #ciere de archivo luego de guardar la informacion 


    def ver_tiempos(self, boton):

        try: #se usa para ejecutar un bloque de codigo (try:)
            archivo = open("tiempos.txt", "r") #Esto permite leer los tiempos guardados ("r" significa leer)
            contenido = archivo.read() #abrir el archivo para leerlo 
            archivo.close() #cierre de el luego de leerlo 
        except:
            contenido = "No hay tiempos guardados"

        popup = Popup( #ventna emeguente para ver informacion de tiempos 
            title="Tiempos guardados", #titulos
            content=Label(text=contenido), #el contenido de la ventana será un Label que mostrará el texto almacenado en contenido
            size_hint=(0.8,0.8) #0.8 significa 80% del ancho y alto de la pantalla.
        )

        popup.open() #para poder abrir ventana 





                        #LINEAS OBLIGATORIAS DE KIVY 
class JuegoApp(App):
    def build(self):
        return JuegoMemoria()


if __name__ == "__main__":
    JuegoApp().run()

    