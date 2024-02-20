from datetime import datetime


class Article:
    def __init__(self, nom, prix, quantite, date_expiration):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        self.date_expiration = datetime.strptime(date_expiration, "%Y-%m-%d")

    def getNom(self):
        return self.nom
    
    def getPrix(self):
        return self.prix
    
    def getQuantite(self):
        return self.quantite

    def getDateExpiration(self):
        return self.date_expiration
    
    def setPrix(self, nouveau_prix):
        self.prix = nouveau_prix
