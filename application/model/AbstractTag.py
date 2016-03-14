from mongoengine import *
from application import app

connect(app.config['DATABASE'], host=app.config['DATABASE_SERVER'])


class AbstractTag(DynamicDocument):
    pubMed_id = StringField()
    title = StringField()
    abstract = StringField()
    terms = StringField()
    generals = StringField()
    category = StringField()
    key_sentence_list = ListField()
