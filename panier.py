from datetime import datetime
from article import Article


class Panier:
    def __init__(self):
        self.articles = []
        self.reduction = None
        self.coupons = {}



    def ajouterArticle(self, prix, nom, quantite, date_expiration):
        trouve = False
        for article in self.articles:
            if article.getNom() == nom and article.getDateExpiration() == datetime.strptime(date_expiration, "%Y-%m-%d"):
                article.augmenterStock(quantite)
                trouve = True
                break
        if not trouve:
            nouvel_article = Article(nom, prix, quantite, date_expiration)
            self.articles.append(nouvel_article)
        self.historique_stock.update(nom, quantite, datetime.now().strftime("%Y-%m-%d"), "add")



    def retirerArticle(self, nom_article, quantite=None):
        for article in self.articles:
            if article.getNom() == nom_article:
                quantite_initiale = article.getQuantite()
                if quantite is None or quantite == quantite_initiale:
                    self.articles.remove(article)
                    self.historique_stock.update(nom_article, quantite_initiale, datetime.now().strftime("%Y-%m-%d"), "remove")
                else:
                    article.reduireStock(quantite)
                    self.historique_stock.update(nom_article, quantite, datetime.now().strftime("%Y-%m-%d"), "remove")
                return
        raise ValueError("L'article n'est pas actuellement en stock.")
        


