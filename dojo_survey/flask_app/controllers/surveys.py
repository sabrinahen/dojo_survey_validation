from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.survey import Dojo

@app.route("/")
def index():
    return render_template("index.html")
    # why dont i have to pass a variable

@app.route("/process", methods=["POST"])
def create_survey():
    data = {
        "name" : request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }
    if not Dojo.validate_dojo(data):
        return redirect ("/")
    Dojo.save(data)
    return redirect("/results")

@app.route('/results')
def results():
    return render_template('success.html', dojo = Dojo.get_last())