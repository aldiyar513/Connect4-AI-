# Connect Four AI

## 🎯 Overview
Connect 4 AI using **Minimax with Alpha-Beta Pruning** and **Iterative Deepening Search**. Plays on a 6×7 grid where players drop discs to get four in a row. The AI blocks threats, creates winning opportunities, and adapts within a time limit.

---

## 🛠 Implementation

### Board Representation
- **NumPy matrix** (6×7 grid)
- `0` = empty, `1` = Player, `2` = AI

### AI Algorithm
- **Minimax** with **Alpha-Beta Pruning** to reduce search space
- **Iterative Deepening** for balanced depth and performance
- **Center column prioritization** for strong opening moves
- Time-limited search to ensure quick AI responses

### Game Logic
- `do_move()` — Places disc in lowest empty row of chosen column
- `make_move()` — Updates board and switches turns
- `terminal()` — Detects wins (horizontal, vertical, diagonal) and draws
- Input validation for player moves

---

## Folder Layout
```
├── connect_four.py      
├── README.md               
└── plots/
```

## 🚀 How to Run
```bash
pip install -r requirements.txt
python connect_four.py
```
