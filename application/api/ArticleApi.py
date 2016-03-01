from application.api.abstract_api import AbstractApi
from application.model.Article import Article
from application.model.AbstractTag import AbstractTag


class ArticleApi(AbstractApi):
    @classmethod
    def rtrv_by_range(cls, start, end):
        return Article.objects[start:end]

    @classmethod
    def rtrv_one(cls, **kwargs):
        articles = AbstractTag.objects(**kwargs)
        if len(articles) > 0:
            return articles[0]
        else:
            articles = Article.objects(**kwargs)
            if len(articles) > 0:
                return articles[0]
        return None

    @classmethod
    def create_tag(cls, _id, terms, general, category):
        article = cls.rtrv_one(pubMed_id=_id)
        if article is not None:
            abstractTag = AbstractTag(
                pubMed_id=_id,
                title=article.title,
                abstract=article.abstract,
                terms=terms,
                generals=general,
                category=category
            )
            abstractTag.save()
            return True
        return False

    @classmethod
    def rtrv_all_tagged_articles(cls):
        articles = AbstractTag.objects()
        id_list = []
        for article in articles:
            id_list.append(article.pubMed_id)
        return id_list
