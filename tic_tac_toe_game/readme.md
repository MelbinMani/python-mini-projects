# 🧠 Tic Tac Toe — Python Console Game

A simple console-based Tic Tac Toe game where you play as **O** against a computer opponent (**X**) that makes random moves. Built with clean backend logic, input validation, and replay support.

---

## 🚀 How to Run

Make sure you have Python installed. Then run:

```bash
python tic_tac_toe.py
```
---

## 🎮 Game Features

- Human vs Computer gameplay
- Input validation for user moves
- Randomized computer moves
- Win/draw detection
- Replay option after each game
- Clean board display using ASCII art

---

## 🧩 Code Structure

- ```display_board(board)``` — prints the current board
- ```free_fields(board)``` — returns list of empty cells
- user(board) — handles user input and validation
- ```computer(board)``` — picks a random empty cell
- ```move(board, position, sign)``` — places a move
- ```victory_for(board, sign)``` — checks for win
- ```check_draw(board)``` — checks for draw
- ```play_game()``` — runs one full game loop
- ```main()``` — handles replay logic

---
## 🛠️ Future Improvements

- Smarter AI (Minimax or rule-based)
- GUI version using Tkinter or Pygame
- Score tracking across rounds
