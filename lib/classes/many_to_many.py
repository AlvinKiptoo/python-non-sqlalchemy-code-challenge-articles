class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        author._articles.append(self)
        
        if not hasattr(magazine, '_articles'):
            magazine._articles = [] 
        magazine._articles.append(self)

        Article.all.append(self)
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Author must be of type Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        self._magazine = new_magazine

    @property
    def title(self):
        return self._title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        self._articles = []
        
    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Name must be a string")
        self._name = new_name

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        contributing_authors = [
            author for author in set([article.author for article in self.articles()])
            if len([article for article in self.articles() if article.author == author]) > 2
        ]
        if not contributing_authors:
            return None
        return contributing_authors