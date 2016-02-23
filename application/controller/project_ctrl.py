from flask import render_template
from application import app


@app.route('/', methods=['GET'])
def homepage():
<<<<<<< HEAD
    return render_template("homepage3.html")
=======
    return render_template("homepage2.html")
>>>>>>> 4f416b02a5b308c783dbdf0513069ed80be0de23


@app.route('/test', methods=['GET'])
def test():
<<<<<<< HEAD
    return render_template("homepage2.html")
=======
    return render_template("homepage.html")
>>>>>>> 4f416b02a5b308c783dbdf0513069ed80be0de23
