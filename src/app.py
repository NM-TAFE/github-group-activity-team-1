from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialise game board and current player
board = [' '] * 9
current_player = 'X'

# NOTE: you cannot use this answer in Portfolio Part 2
def check_winner():
    """
    Check for a winner in the game.
    This function should check all possible winning combinations on the board.
    Returns:
        Todo ?
    """

    return None


def check_draw():
    """
    Check if current state is a draw.

    It's a draw if the board does not have any free moves and there is no winner.

    Returns:
        Todo ?
    """
    return ' ' not in board


@app.route('/')
def index():
    """
    Load the game board and display the current game state.

    Renders the 'index.html' template with the current state of the game including
    the board, the current player, and whether there's a winner or a draw.

    """
    winner = check_winner()
    draw = check_draw()
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)


@app.route('/play/<int:cell>')
def play(cell):
    """
    Updates the board with the current player's move if the selected cell is empty.
    """
    # breakpoint()
    global current_player
    if board[cell] == ' ':
        board[cell] = current_player
        if not check_winner():
            current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))


@app.route('/reset')
def reset():
    """
    Reset the game to the initial state.
    """
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    return redirect(url_for('index'))


app.run(debug=True)
