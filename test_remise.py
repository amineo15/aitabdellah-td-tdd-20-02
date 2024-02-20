import pytest
from panier import Panier
from datetime import datetime, timedelta




@pytest.fixture
def stock():
    panier = Panier()
    date1 = datetime.now().strftime("%Y-%m-%d")
    date2 = (datetime.now() - timedelta(days=21)).strftime("%Y-%m-%d")
    panier.ajouterArticle("viande", 1.3, 10, date1)
    panier.ajouterArticle("tomate", 2, 4, date2)
    return panier
