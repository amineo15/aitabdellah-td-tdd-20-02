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



def test_ajouter_coupon(stock, capsys):
    with pytest.raises(ValueError) as e:
        stock.addCoupon("NADA", 0, "viande")
    assert str(e.value) == "La réduction doit être supérieure à 0."

    stock.addCoupon("CODE20", 20, "viande")

    with pytest.raises(ValueError) as e:
        stock.addCoupon("CODE20", 20, "tomate")
    assert str(e.value) == "Ce coupon a déjà été appliqué a un article."

    with pytest.raises(ValueError) as e:
        stock.addCoupon("NEWCODE", 20, "viande")
    assert str(e.value) == "L'article possède déjà un coupon."



def test_prix_article_ne_negatif_apres_remise(stock):
    stock.ajouterArticle("pain", 1.8, 15, "2024-05-01")
    stock.addCoupon("CODE30", 30, "pain")
    assert stock.prix >= 0
