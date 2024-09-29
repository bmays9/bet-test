from flask import render_template
from betting import app, db
from betting.models import User, Line, Bet

@app.route("/")
def home():
    return render_template("base.html")