from flask import render_template
from application import app


@app.route('/', methods=['GET'])
def homepage():
    return render_template("pages/homepage.html")


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("pages/dashboard.html")
