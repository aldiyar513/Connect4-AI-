# Connect Four AI — Minimax with Alpha-Beta Pruning & Iterative Deepening

## 🎯 Introduction
During my time in San Francisco, I noticed the popularity of Connect 4 among teenagers and became interested in implementing an AI opponent for this classic board game.

Connect 4 is played on a **6×7 grid**, where players take turns dropping colored discs from the top. The first player to align four discs horizontally, vertically, or diagonally wins.

With over **4.5 trillion possible board configurations** (4,531,985,219,092 to be exact), the game is simple to play but complex to master. While the second player has more potential winning paths, **perfect play from the first player guarantees victory**. Draws are rare but possible.

### 📌 Project Goals
The AI in this project is designed to:
- Run efficiently on common devices
- Calculate optimal moves that maximize utility
- Select the best possible move for any given board state

---

## ⚡ Challenges & Obstacles
1. **Computational Complexity** — Trillions of combinations make exhaustive search infeasible.
2. **Strategic Decision-Making** — Must balance offense (maximizing AI utility) and defense (blocking opponent wins).
3. **Game State Evaluation** — Correctly detect terminal states (win, lose, draw).
4. **User Interface** — Display board clearly, handle player inputs, and reject invalid moves.
5. **Performance Constraints** — Compute moves quickly enough to maintain engagement.

---

## 🛠 Implementation Details

### Board Representation
- The board is stored as a **NumPy matrix** of size `rows × columns` (default: `6 × 7`).
- `0` = empty cell  
- `1` = Player (Human)  
- `2` = AI  

### Move Handling
- **`do_move()`** places the disc in the lowest empty row of the chosen column.
- **`make_move()`** updates the board and switches the turn (`self.turn = 3 - self.turn`).

### Terminal State Detection
- **`terminal()`** checks for:
  - Horizontal wins
  - Vertical wins
  - Diagonal-up wins
  - Diagonal-down wins
  - Draw (full board, no winner)

### AI Algorithm
The AI uses **Minimax with Alpha-Beta Pruning** to reduce the search space and **Iterative Deepening Search** to balance speed and optimality.

**Key features:**
- Center column prioritization (common winning strategy)
- Depth-limited search
- Time-limited search for responsiveness

### Performance Tracking
- Execution time for AI moves is recorded in `time_keeper`.
- Handles invalid inputs gracefully.

---

## 🚀 How to Run
1. **Clone the repository**
```
git clone https://github.com/YOUR_USERNAME/connect-four-ai.git
cd connect-four-ai
```
2. **Install dependencies**
```
pip install -r requirements.txt
```
3. **Run the game**
```
python connect_four.py
```

---

## 📊 Performance Analysis

### 1. Strategy
- AI prioritizes the center column when going first — a commonly strong opening.

### 2. Time Distribution
- Move computation time is tracked and can be visualized via plots (see below).

### 3. Input Handling
- Rejects invalid moves and re-prompts until valid input is received.

### 4. Search Depth
- Early game: shallower depth due to branching factor.
- Mid/late game: deeper search as more pruning occurs.

### 5. Gameplay Quality
- AI blocks imminent winning moves from the player.
- Capable of forcing wins from advantageous positions.

---

## 📈 Graphs

After a game (or using the simulator), generate plots:

```
# one-time: install matplotlib (already in requirements.txt)
pip install -r requirements.txt

# in Python:
import metrics_and_plots as mp
mp.attach_hooks()

# Option A: play your normal Human vs AI game in your main script, then:
mp.save_plots()

# Option B: quickly simulate AI vs Random to create data:
mp.simulate_ai_vs_random(num_moves=16, search_time=1.5)
mp.save_plots()
```

This will create:
- `plots/move_time_over_turns.png`
- `plots/depth_over_turns.png`
- `plots/nodes_explored_over_turns.png`

You can embed them in the README if desired:
```
![Move Time](plots/move_time_over_turns.png)
![Depth](plots/depth_over_turns.png)
![Nodes](plots/nodes_explored_over_turns.png)
```

---

## 📂 File Structure
```
connect-four-ai/
│
├── connect_four.py           # Main game code (unchanged)
├── metrics_and_plots.py      # Add-on: metrics hooks + plot export
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
└── plots/                    # Generated figures will be saved here
```

---

## 📜 Notes
- Grammarly AI was used to correct grammatical errors in documentation.
- Reference: Cahn (2024), Connect Four strategy and combinatorics.
