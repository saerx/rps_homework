from flask import render_template, request, redirect
from app import app
from app.models.player import Player
from app.models.game import Game



@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title="Welcome")

@app.route('/<first_hand>/<second_hand>')
def play_rps(first_hand, second_hand):

    # player_1_hand = request.form["player_1_hand"]
    # player_2_hand = request.form["player_2_hand"]

    player_1 = Player("Player one", first_hand)
    player_2 = Player("Player two", second_hand)

    game_1 = Game(player_1, player_2)

    winner = game_1.find_winner()

    return render_template('result.html', winner=winner)


# @app.route('/play_rps', methods=["POST"])
# def play_rps():

#     player_1_hand = request.form["player_1_hand"]
#     player_2_hand = request.form["player_2_hand"]

#     player_1 = Player("Player 1", player_1_hand)
#     player_2 = Player("Player 2", player_2_hand)

#     game_1 = Game(player_1, player_2)

  