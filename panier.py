from datetime import datetime


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
