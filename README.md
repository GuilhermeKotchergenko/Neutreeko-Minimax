# Neutreeko AI

This repository contains a Python implementation of the abstract strategy board game **Neutreeko**, featuring an artificial intelligence (AI) opponent. The project was developed as part of the *Artificial Intelligence and Data Science Elements* course at the Faculty of Sciences, University of Porto (FCUP).

## Features

- **Game Modes**:
  - **Player vs Player**: Play locally against a friend on the same machine.
  - **Player vs AI**: Challenge the computer with adjustable difficulty levels (Easy, Medium, Hard).
- **AI Algorithm**: Utilizes Minimax with Alpha-Beta pruning for strategic decision-making.
- **Theme**: Includes a custom character theme ("Tia").
- **Graphics**: Built using the Pygame library.

## Prerequisites

Ensure you have the following installed on your system:
- **Python 3.8+** (Tested with Python 3.13.9)
- **Pygame 2.0.1+** (Tested with Pygame 2.6.1)

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/GuilhermeKotchergenko/Neutreeko-Minimax.git
    cd Neutreeko-Minimax
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

## AI Difficulty Levels

The game features three AI difficulty levels, each using the Minimax algorithm with Alpha-Beta pruning but with different search depths and evaluation strategies:

### Easy
- **Strategy**: Random evaluation
- **Search Depth**: 1 move ahead
- **Behavior**: Makes random moves with minimal lookahead, suitable for beginners

### Medium
- **Strategy**: Heuristic-based evaluation with pattern recognition
- **Search Depth**: 3 moves ahead
- **Heuristics**:
  - Detects "2-in-a-row" patterns (two pieces aligned with one empty space to complete a line)
  - Assigns high priority to blocking opponent threats (weighted 1.5x higher than building own lines)
  - Evaluates center control for better mobility
  - Scores potential winning lines and defensive positions

### Hard
- **Strategy**: Same heuristic evaluation as Medium
- **Search Depth**: 4 moves ahead
- **Behavior**: Looks further into the future, making it significantly stronger and more strategic

### Performance Notes
Based on simulation testing (180+ games):
- Hard and Medium AI consistently defeat Easy AI (100% win rate)
- The first player (Black) has a significant advantage at higher difficulty levels
- Hard AI can analyze ~160,000 board positions per move at depth 4

## Testing

Run the AI simulation grid to test different difficulty matchups:

```bash
python tests/sim_ai_grid.py
```

This will run 20 games for each combination of difficulty levels and display win statistics. Numbers of games are set to 20 for performance reasons but adjustable.

---

*This project is for educational purposes.*
