from flask import render_template, request, redirect, url_for
from betting import app, db
from betting.models import User, Line, Bet, Team, Country

@app.route("/")
def home():
    return render_template("base.html")


@app.route("/manage_teams")
def manage_teams():
    countries = list(Country.query.order_by(Country.country_name).all())
    return render_template("manage_teams.html")


@app.route("/add_country", methods = ["POST"])
def add_country():
    if request.method == "POST":
        country = Country(country_name=request.form.get("country_name"))
        db.session.add(country)
        db.session.commit()
        return redirect(url_for("manage_teams"))
    
    return render_template("manage_teams.html")
    