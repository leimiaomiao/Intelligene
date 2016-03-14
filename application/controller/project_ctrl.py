from flask import render_template, request, jsonify
from application.api.ArticleApi import ArticleApi
from application import app
import nltk


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
        return render_template("pages/tag.html", articles=articles, tagged_id_list=tagged_id_list,
                               target_modal="wordModal")
    else:
        _id = request.form['pubMed_id']
        category = request.form['category']
        terms = request.form['terms']
        general = request.form['general']

        result = ArticleApi.create_tag(_id, terms, general, category)
        return jsonify(
            data={
                "id": _id,
                "category": category
            }
        )


@app.route('/tag/sentence', methods=['GET'])
def tag_sentence():
    articles = ArticleApi.rtrv_by_range(990, 1090)
    tagged_id_list = ArticleApi.rtrv_all_tagged_articles()
    return render_template("pages/tag.html", articles=articles, tagged_id_list=tagged_id_list,
                           target_modal="sentenceModal")


@app.route('/tag/sentence/<_id>', methods=['GET', 'POST'])
def tag_one_sentence(_id):
    if request.method == 'GET':
        article = ArticleApi.rtrv_one(pubMed_id=_id)
        abstract = article.abstract
        tagged_sentence_list = ArticleApi.rtrv_tagged_sentence_list(_id)

        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = sent_detector.tokenize(abstract)

        return jsonify(
            data=render_template("pages/sentences.html", sentences=sentences, article=article,
                                 tagged_sentence_list=tagged_sentence_list)
        )
    else:
        sentence_list = []
        for s in (request.form.getlist(key) for key in request.form.keys()):
            sentence_list.append(s[0])
        ArticleApi.create_tag_sentence(_id, sentence_list)
        return jsonify(
            data={
                "id": _id,
                "result": "success"
            }
        )


@app.route('/tag_one/<_id>', methods=['GET'])
def tag_one(_id):
    return jsonify(
        data=render_template("pages/oneArticle.html", article=ArticleApi.rtrv_one(pubMed_id=_id))
    )
