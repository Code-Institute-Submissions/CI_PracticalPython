import os
import json
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", page_title="Home")

@app.route('/about')
def about():
    return render_template("about.html", page_title="About")

@app.route('/game')
def game():
    return render_template("game.html", page_title="Game")
    
@app.route('/contact')
def contact():
    return render_template("contact.html",page_title="Contact")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)