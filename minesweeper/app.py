from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)
ROWS, COLS, MINES = 16, 16, 40
game = {}


def new_game():
    game.update(mines=set(), opened=set(), flags=set(), over=False, won=False)


def neighbors(r, c):
    return [(r + i, c + j) for i in (-1, 0, 1) for j in (-1, 0, 1)
            if (i or j) and 0 <= r + i < ROWS and 0 <= c + j < COLS]


def count(r, c):
    return sum(n in game["mines"] for n in neighbors(r, c))


def state():
    board = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            p = (r, c)
            if p in game["opened"] or (game["over"] and p in game["mines"]):
                row.append("*" if p in game["mines"] else count(r, c))
            else:
                row.append("🚩" if p in game["flags"] else "")
        board.append(row)
    return jsonify(board=board, over=game["over"], won=game["won"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reference")
def reference():
    return render_template("reference.html")


@app.route("/new")
def new():
    new_game()
    return state()


@app.route("/state")
def get_state():
    return state()


@app.route("/open", methods=["POST"])
def open_cell():
    r, c = request.json["r"], request.json["c"]
    p = (r, c)
    if game["over"] or p in game["flags"] or p in game["opened"]:
        return state()
    if not game["mines"]:  # place mines after first click so it is always safe
        safe = {p, *neighbors(r, c)}
        cells = [(i, j) for i in range(ROWS) for j in range(COLS) if (i, j) not in safe]
        game["mines"] = set(random.sample(cells, MINES))
    if p in game["mines"]:
        game["over"] = True
        return state()
    stack = [p]
    while stack:  # flood fill empty areas
        cur = stack.pop()
        if cur in game["opened"] or cur in game["flags"]:
            continue
        game["opened"].add(cur)
        if count(*cur) == 0:
            stack.extend(neighbors(*cur))
    if len(game["opened"]) == ROWS * COLS - MINES:
        game["over"] = game["won"] = True
    return state()


@app.route("/flag", methods=["POST"])
def flag():
    p = (request.json["r"], request.json["c"])
    if not game["over"] and p not in game["opened"]:
        game["flags"] ^= {p}
    return state()


new_game()

if __name__ == "__main__":
    app.run(debug=True)
