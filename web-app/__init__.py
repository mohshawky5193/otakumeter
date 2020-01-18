# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 00:32:45 2020

@author: mam22
"""

from flask import Flask, render_template

app = Flask(__name__)

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
    return "quiz"
if __name__ == "__main__":
    app.run()