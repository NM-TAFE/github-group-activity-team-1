from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialise game board and current player
board = [' '] * 9
current_player = 'X'

# NOTE: you cannot use this answer in Portfolio Part 2
def check_winner():
    # Winning combinations
    winning_conditions = [[0, 4, 8], [2, 4, 6],  # diagnols
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],  # column
                          [0, 1, 2], [3, 4, 5], [6, 7, 8]]  # row

    for combo in winning_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    return None


def check_draw():
    return ' ' not in board


@app.route('/')
def index():
    winner = check_winner()
    draw = check_draw()
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()
    global current_player
    if board[cell] == ' ':
        board[cell] = current_player
        if not check_winner():
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    return redirect(url_for('index'))


app.run(debug=True)
