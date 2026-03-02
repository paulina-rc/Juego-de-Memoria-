from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random


class JuegoMemoria(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 4
        
        # imagenes 
        self.imagenes = [
            "img/Beso.jpg",
            "img/Brillo.png",
            "img/Cereza.png",
            "img/Corona.png",
            "img/Diamante.jpg",
            "img/Estrella.png",
            "img/Flores.jpg",
            "img/Mono.png",
        ] * 2

        random.shuffle(self.imagenes)

        for imagen in self.imagenes:
            boton = Button(
                background_normal="img/Pregunta.jpg",
                background_down="img/Pregunta.png"
            )

            # guardamos qué imagen le pertenece
            boton.imagen_real = imagen

            boton.bind(on_press=self.cambiar_imagen)
            self.add_widget(boton)

    def cambiar_imagen(self, boton):
        boton.background_normal = boton.imagen_real
        boton.background_down = boton.imagen_real


class JuegoApp(App):
    def build(self):
        return JuegoMemoria()


if __name__ == "__main__":
    JuegoApp().run()