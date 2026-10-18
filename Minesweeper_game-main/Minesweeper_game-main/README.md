# Minesweeper (Flask)

A simple Minesweeper game built with Python Flask. The game runs in your browser, and all game logic is handled by the Flask backend.

## Features

- 16 x 16 board with 40 hidden mines
- Your first click is always safe
- Empty areas open automatically (flood fill)
- Right click to place or remove a red flag 🚩
- Win and game over detection
- Separate **Game** and **About** pages
- Simple, light styling

## Tech Stack

- Python 3
- Flask
- HTML, CSS and JavaScript (no extra libraries)

## Project Structure

```
minesweeper/
├── app.py                  # Flask app and game logic
├── requirements.txt        # Python dependencies
├── static/
│   └── favicon.png         # Browser tab icon
└── templates/
    ├── base.html           # Shared layout, menu and styling
    ├── index.html          # Game page
    └── about.html          # How to play (Bangla + English)
```

## How to Run

1. Make sure Python 3 is installed.
2. Clone the repository and go into the folder:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux / macOS
   venv\Scripts\activate         # Windows
   ```

4. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   python app.py
   ```

6. Open your browser and go to **http://127.0.0.1:5000**

## How to Play

- **Left click** a box to open it.
- **Right click** a box to place or remove a flag 🚩.
- A number shows how many mines are touching that box, including diagonals.
- Open a mine and you lose. Open every safe box and you win.
- Click **New Game** to start again.

## Tips and Tricks

- Start in a corner or on an edge, where there are fewer neighbors to guess.
- If a "1" has only one closed box next to it, that box is a mine.
- If a number already has enough flags around it, all its other neighbors are safe.
- Use flags to mark mines you are sure about, so you don't click them by mistake.

## Customize

To change the board size or the number of mines, edit this line in `app.py`:

```python
ROWS, COLS, MINES = 16, 16, 40
```

Note: the game state is stored in one global variable on the server, so it supports one player at a time.

## Credits

- Favicon icon by [Icons8](https://icons8.com/).
