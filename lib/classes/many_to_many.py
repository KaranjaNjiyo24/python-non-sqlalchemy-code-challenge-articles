class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            return
        if len(title) < 5 or len(title) > 50:
            return
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        pass
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        mags_categories = [article.magazine.category for article in self.articles()]
        unique_categories = list(set(mags_categories)) if mags_categories else None
        return unique_categories

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.article():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        exceptional_authors = [author for author, count in author_counts.items() if count > 2]
        return exceptional_authors if exceptional_authors else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all or not Article.all:
            return None
        magazine_article_counts = {}
        for article in Article.all:
            magazine_article_counts[article.magazine] = magazine_article_counts.get(article.magazine, 0) + 1
        return max(magazine_article_counts, key = magazine_article_counts.get)
