from kivy.app import App #libreria de Kivy 
from kivy.uix.gridlayout import GridLayout #libreria de Kivy 
from kivy.uix.button import Button #libreria de Kivy 
import random


class JuegoMemoria(GridLayout):

    def __init__(self, **kwargs): #Esta función se ejecuta automáticamente cuando se crea el objeto
                                    #Ejemplo: tablero = juego de memoria 
        super().__init__(**kwargs) #**Kwargs son parametros que se ponen por default

        self.cols = 4 #asigna 4 columnas al tablero 
        
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

    def cambiar_imagen(self, boton): #funcion que revela la carta cuando se preciona 
        boton.background_normal = boton.imagen_real #remplazo de imagen
        boton.background_down = boton.imagen_real #remplazo de imagen


class JuegoApp(App):
    def build(self):
        return JuegoMemoria()


if __name__ == "__main__":
    JuegoApp().run()