#Memory Game — Kivy

An interactive **Memory Card Game** built with **Python** and **Kivy**. Flip cards, find matching pairs, track your time and movements — and compete against a friend in multiplayer mode!

---

## Gameplay Preview

> Two players compete to find the most matching pairs. On every failed attempt, the turn switches. The player with the most pairs at the end wins!
---
## Features

| Feature | Description |
|---------|-------------|
|  Card Board | 4x4 grid with hidden image cards |
|  Pair Matching | Automatic comparison when 2 cards are flipped |
|  Solo Mode | Play alone and beat your own time |
|  Multiplayer Mode | Two players compete turn by turn |
|  Score System | Points tracked per player in real time |
|  Timer | Counts seconds from the first move |
|  Move Counter | Tracks how many pairs you've flipped |
|  Time Records | Saves each game result to `tiempos.txt` |
|  History Viewer | Pop-up showing all saved game times |
---
##  Game Modes

### Solo Mode
Play by yourself and try to find all 8 pairs in the shortest time possible. Your time is saved automatically when you finish.

### Multiplayer Mode
Two players take turns flipping cards:
-  Find a pair → **keep your turn**
-  No match → **turn passes to the other player**
-  At the end, the player with the most pairs **wins**
---
## Tech Stack

- **Python 3** — Core programming language
- **Kivy** — Cross-platform GUI framework
- **OOP** — Object-oriented design with classes and events
- **File I/O** — `.txt` file for storing game history
- **Clock & Popups** — Kivy's built-in timer and modal windows
---
## Project Structure
```
Juego-de-Memoria/
│
├── img/
│   ├── Beso.jpg
│   ├── Brillo.png
│   ├── Cereza.png
│   ├── Corona.png
│   ├── Diamante.jpg
│   ├── Estrella.png
│   ├── Flores.jpg
│   ├── Mono.png
│   └── Pregunta.jpg       # Card back image
│
├── Main.py                # Main game logic
├── tiempos.txt            # Auto-generated game history
└── README.md
```

##  How to Run

### 1. Make sure Python is installed
```bash
python --version
```
### 2. Install Kivy
```bash
pip install kivy
```
### 3. Run the game
```bash
python Main.py
```
---
## How It Works (Technical Overview)

The game is built using a single class `JuegoMemoria` that extends Kivy's `BoxLayout`. Here's a quick breakdown:

- **`__init__`** — Sets up the board, shuffles images, builds the UI
- **`elegir_modo`** — Pop-up to choose Solo or Multiplayer
- **`cambiar_imagen`** — Reveals a card when clicked
- **`comparar_cartas`** — After 1 second, checks if 2 flipped cards match
- **`guardar_tiempo`** — Appends the result to `tiempos.txt` with date and time
- **`ver_tiempos`** — Opens a pop-up showing the full game history

---

## Author

**Paulina Rojas** — [@paulina-rc](https://github.com/paulina-rc)

> Academic project — Computer Science & Web Development, 11th Grade
