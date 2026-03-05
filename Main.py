from kivy.app import App #libreria de Kivy 
from kivy.uix.gridlayout import GridLayout #libreria de Kivy 
from kivy.uix.button import Button #libreria de Kivy 
from kivy.uix.label import Label #para mostrar texto
from kivy.uix.popup import Popup #para mostrar ventana de tiempos
from kivy.clock import Clock #libreria para temporizadores
from datetime import datetime #para guardar fecha
import random


class JuegoMemoria(GridLayout):

    def __init__(self, **kwargs): #Esta función se ejecuta automáticamente cuando se crea el objeto
                                    #Ejemplo: tablero = juego de memoria 
        super().__init__(**kwargs) #**Kwargs son parametros que se ponen por default

        self.cols = 4 #asigna 4 columnas al tablero 
        
        # lista donde se guardan las cartas abiertas
        self.cartas_seleccionadas = []

        # contador de movimientos del jugador
        self.movimientos = 0

        # contador de pares encontrados
        self.pares_encontrados = 0

        # contador de tiempo
        self.tiempo = 0

        # label que muestra el tiempo en pantalla
        self.label_tiempo = Label(text="Tiempo: 0", size_hint=(1,0.1))
        self.add_widget(self.label_tiempo)

        # label que muestra movimientos
        self.label_movimientos = Label(text="Movimientos: 0", size_hint=(1,0.1))
        self.add_widget(self.label_movimientos)

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


    def actualizar_tiempo(self, dt):

        # aumentar tiempo cada segundo
        self.tiempo += 1
        self.label_tiempo.text = "Tiempo: " + str(self.tiempo)


    def cambiar_imagen(self, boton):

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

        else:
            # si coinciden aumentamos pares encontrados
            self.pares_encontrados += 1

        # limpiar lista
        self.cartas_seleccionadas = []

        # verificar si el juego terminó
        if self.pares_encontrados == 8:

            # detener el temporizador
            Clock.unschedule(self.actualizar_tiempo)

            # guardar tiempo
            self.guardar_tiempo()

            # mostrar ventana de victoria
            mensaje = "¡Ganaste!\nTiempo: " + str(self.tiempo) + " segundos"

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