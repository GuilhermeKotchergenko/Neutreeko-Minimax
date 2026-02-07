# Neutreeko AI

This repository contains a Python implementation of the abstract strategy board game **Neutreeko**, featuring an artificial intelligence (AI) opponent. The project was developed as part of the *Artificial Intelligence and Data Science Elements* course at the Faculty of Sciences, University of Porto (FCUP).

## Features

- **Game Modes**:
  - **Player vs Player**: Play locally against a friend on the same machine.
  - **Player vs AI**: Challenge the computer with adjustable difficulty levels.
- **AI Algorithm**: Utilizes Minimax with Alpha-Beta pruning for strategic decision-making.
- **Theme**: Includes a custom character theme ("Tia").
- **Graphics**: Built using the Pygame library.

## Prerequisites

Ensure you have the following installed on your system:
- **Python 3.8+**
- **Pygame 2.0.1+**

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/GuilhermeKotchergenko/ElementosIACD.git
    cd ElementosIACD
    ```

2.  **Install dependencies**:
    ```bash
    pip install pygame
    ```

## How to Run

Execute the main script to launch the game:

```bash
python main.py
```

## How to Play

1.  **Objective**: Align three of your pieces horizontally, vertically, or diagonally.
2.  **Movement**: Pieces slide in one of the eight directions until they hit an obstacle (another piece or the board edge).
3.  **Controls**: Use the mouse to select a piece, then click on a highlighted valid destination to move it.

---

*This project is for educational purposes.*
