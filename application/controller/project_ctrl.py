from flask import render_template, request, jsonify
from application.api.ArticleApi import ArticleApi
from application import app


@app.route('/', methods=['GET'])
def homepage():
    return render_template("pages/homepage.html")


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("pages/dashboard.html")


@app.route('/tag', methods=['GET', 'POST'])
def tag():
    if request.method == 'GET':
        articles = ArticleApi.rtrv_by_range(0, 100)
        tagged_id_list = ArticleApi.rtrv_all_tagged_articles()
        return render_template("pages/tag.html", articles=articles, tagged_id_list=tagged_id_list)
    else:
        _id = request.form['pubMed_id']
        category = request.form['category']
        terms = request.form['terms']
        general = request.form['general']

        result = ArticleApi.create_tag(_id, terms, general, category)
        return jsonify(
            data={
                "id":_id,
                "category": category
            }
        )


@app.route('/tag_one/<_id>', methods=['GET'])
def tag_one(_id):
    return jsonify(
        data=render_template("pages/oneArticle.html", article=ArticleApi.rtrv_one(pubMed_id=_id))
    )
