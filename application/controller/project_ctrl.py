from flask import render_template
from application import app


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage2.html")


@app.route('/test', methods=['GET'])
def test():
    return render_template("homepage.html")