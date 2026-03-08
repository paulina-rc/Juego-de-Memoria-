# 🧠 Juego de Memoria

Este proyecto consiste en el desarrollo de un **juego de memoria interactivo** programado en **Python utilizando la librería Kivy**.
El objetivo del juego es encontrar pares de cartas iguales mientras se registra el tiempo y los movimientos realizados durante la partida.

El proyecto fue desarrollado como parte de un proceso de aprendizaje en **desarrollo de interfaces gráficas y lógica de programación**, integrando conceptos como manejo de eventos, control del flujo del juego y almacenamiento de datos.

---

# 🎮 Características del juego

El juego incluye las siguientes funcionalidades:

* Tablero de cartas con imágenes ocultas.
* Sistema de **comparación de pares**.
* Contador de **movimientos realizados**.
* Temporizador que mide la duración de la partida.
* **Modo solitario** para jugar individualmente.
* **Modo multijugador**, donde dos jugadores pueden competir.
* Sistema de **turnos entre jugadores**.
* Contador de **puntos por jugador**.
* Registro del **tiempo de cada partida** en un archivo externo.
* Visualización del **historial de tiempos guardados**.

---

# 👥 Modos de juego

## Modo Solitario

El jugador intenta encontrar todos los pares en el menor tiempo posible.

## Modo Multijugador

Dos jugadores compiten para encontrar la mayor cantidad de pares.

* Si un jugador encuentra un par, **puede jugar nuevamente**.
* Si falla, **el turno pasa al otro jugador**.
* Al finalizar el juego se muestra el **ganador**.

---

# ⚙️ Tecnologías utilizadas

* **Python**
* **Kivy** (desarrollo de interfaz gráfica)
* Manejo de archivos `.txt` para almacenamiento de datos
* Programación orientada a objetos

---

# 📂 Estructura del proyecto

```
Juego-de-Memoria/
│
├── img/           # imágenes utilizadas en las cartas
├── Main.py        # código principal del juego
├── Tiempos.txt    # archivo donde se guardan los tiempos de las partidas
└── README.md      # documentación del proyecto
```

---

# ▶️ Cómo ejecutar el proyecto

1. Instalar Python.
2. Instalar la librería Kivy.

```
pip install kivy
```

3. Ejecutar el archivo principal.

```
python Main.py
```

---

# 📌 Funcionalidades implementadas

* Interfaz gráfica interactiva.
* Comparación automática de cartas.
* Sistema de turnos en multijugador.
* Registro de resultados.
* Ventanas emergentes para interacción con el usuario.

---

# 📚 Objetivo del proyecto

El objetivo de este proyecto es aplicar conocimientos de programación para desarrollar una **aplicación interactiva con interfaz gráfica**, integrando lógica de juego, manejo de eventos y almacenamiento de información.

---

# 👩‍💻 Autor

Desarrollado por **Paulina RC**.
Proyecto académico de informática.
