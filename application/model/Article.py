from mongoengine import *
from application import app

connect(app.config['DATABASE'], host=app.config['DATABASE_SERVER'])


class _Author(DynamicEmbeddedDocument):
    name_ = StringField()
    address = StringField()

    lastName = StringField()
    foreName = StringField()
    initials = StringField()
    affiliationInfo = StringField()


class Article(DynamicDocument):
    title = StringField()
    journal = StringField()
    author_list = ListField(EmbeddedDocumentField('_Author'))
    publish_info = StringField()
    abstract = StringField()
    pubMed_id = LongField(required=True)
    keywords = StringField()

    journal_abbre = StringField()
    keyword_list = ListField()
