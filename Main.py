from kivy.app import App #libreria de Kivy 
from kivy.uix.gridlayout import GridLayout #libreria de Kivy 
from kivy.uix.button import Button #libreria de Kivy 
from kivy.clock import Clock #libreria para temporizadores
import random
from kivy.uix.label import Label
from kivy.clock import Clock


class JuegoMemoria(GridLayout):

    def __init__(self, **kwargs): #Esta función se ejecuta automáticamente cuando se crea el objeto
                                    #Ejemplo: tablero = juego de memoria 
        super().__init__(**kwargs) #**Kwargs son parametros que se ponen por default

        self.cols = 4 #asigna 4 columnas al tablero 
        self.cartas_seleccionadas = []  # lista donde se guardan las cartas abiertas
        self.movimientos = 0 # contador de movimientos del jugador

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

    def cambiar_imagen(self, boton):

        if boton in self.cartas_seleccionadas: #evita presionar un carta ya volteada 
            return

        boton.background_normal = boton.imagen_real #muestra la imagen real 
        boton.background_down = boton.imagen_real

        
        self.cartas_seleccionadas.append(boton) #guardar carta ya seleccionada 

        if len(self.cartas_seleccionadas) == 2: #condicion para ver si hay dos cartas abiertas

            self.movimientos += 1 #suma de movimientos, 2 cartas volteadas cuentan como un movimiento 
            print("Movimientos:", self.movimientos)

            Clock.schedule_once(self.comparar_cartas, 1) #tiempo de espera antes de comaparar

    def comparar_cartas(self, dt): #fucion para comparar 

        carta1 = self.cartas_seleccionadas[0]
        carta2 = self.cartas_seleccionadas[1]

        if carta1.imagen_real != carta2.imagen_real:

            #si las cartas no funcionan se vuleven a ocultar 
            carta1.background_normal = "img/Pregunta.jpg"
            carta1.background_down = "img/Pregunta.jpg"

            carta2.background_normal = "img/Pregunta.jpg"
            carta2.background_down = "img/Pregunta.jpg"

        # limpiar lista
        self.cartas_seleccionadas = []


class JuegoApp(App):
    def build(self):
        return JuegoMemoria()


if __name__ == "__main__":
    JuegoApp().run()