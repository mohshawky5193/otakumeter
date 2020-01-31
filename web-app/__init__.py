# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 00:32:45 2020

@author: mam22
"""

from flask import Flask, render_template,request,jsonify,session
from get_anime_characters_from_database import get_anime_characters_for_quiz
import gc

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def homepage():
    return render_template("main.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/howto')
def how_to_play():
    return render_template("how-to-play.html")
@app.route('/quiz')
def quiz():
    return render_template("quiz.html")
@app.route('/get-characters')
def get_characters():
    all_anime_characters= get_anime_characters_for_quiz()
    return jsonify(characters=all_anime_characters)
if __name__ == "__main__":
    app.run(debug=False)