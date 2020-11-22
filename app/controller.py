from flask import render_template
from app import app



@app.route('/')
def index():
    return render_template('index.html', title='Game')

# @app.route('/<first_hand>/<second_hand>')
# def play_rps()
