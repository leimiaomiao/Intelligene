from application.api.abstract_api import AbstractApi
from application.model.Article import Article
from application.model.AbstractTag import AbstractTag
from mongoengine import DoesNotExist


class ArticleApi(AbstractApi):
    @classmethod
    def rtrv_by_range(cls, start, end):
        return Article.objects[start:end]

    @classmethod
    def rtrv_one_article(cls, **kwargs):
        try:
            article = Article.objects.get(**kwargs)
            return article
        except DoesNotExist:
            return None

    @classmethod
    def rtrv_one_abstract(cls, **kwargs):
        try:
            article = AbstractTag.objects.get(**kwargs)
            return article
        except DoesNotExist:
            return None

    @classmethod
    def rtrv_one(cls, **kwargs):
        abstract = cls.rtrv_one_abstract(**kwargs)
        return abstract if abstract is not None else cls.rtrv_one_article(**kwargs)

    @classmethod
    def create_tag(cls, _id, terms, general, category, key_sentence_list=[]):
        article = cls.rtrv_one_article(pubMed_id=_id)
        abstract = cls.rtrv_one_abstract(pubMed_id=_id)
        if abstract is None:
            if article is not None:
                abstractTag = AbstractTag(
                    pubMed_id=_id,
                    title=article.title,
                    abstract=article.abstract,
                    terms=terms,
                    generals=general,
                    category=category,
                    key_sentence_list=key_sentence_list
                )
                abstractTag.save()
                return True
        else:
            abstract.terms = terms
            abstract.generals = general
            abstract.category = category
            abstract.key_sentence_list = key_sentence_list
            abstract.save()
            return True
        return False

    @classmethod
    def create_tag_sentence(cls, _id, key_sentence_list=[]):
        article = cls.rtrv_one_article(pubMed_id=_id)
        abstract = cls.rtrv_one_abstract(pubMed_id=_id)
        if abstract is None:
            if article is not None:
                abstractTag = AbstractTag(
                    pubMed_id=_id,
                    title=article.title,
                    abstract=article.abstract,
                    key_sentence_list=key_sentence_list
                )
                abstractTag.save()
                return True
        else:
            abstract.key_sentence_list = key_sentence_list
            abstract.save()
            return True
        return False

    @classmethod
    def rtrv_all_tagged_articles(cls):
        articles = AbstractTag.objects()
        id_list = []
        for article in articles:
            id_list.append(int(article.pubMed_id))
        return id_list

    @classmethod
    def rtrv_tagged_sentence_list(cls, _id):
        abstract_tag = cls.rtrv_one_abstract(pubMed_id=_id)
        sentence_list = []
        if abstract_tag is not None:
            for s in abstract_tag.key_sentence_list:
                sentence_list.append(s.rstrip())
        return sentence_list
