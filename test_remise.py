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



def test_ajouter_coupon_deja_applique(stock, capsys):
    stock.addCoupon("CODE20", 20, "viande")
    with pytest.raises(ValueError) as e:
        stock.addCoupon("CODE20", 20, "tomate")
    assert str(e.value) == "Ce coupon a déjà été appliqué a un article."




def test_prix_article_ne_negatif_apres_remise(stock):
    stock.ajouterArticle("pain", 1.8, 15, "2024-05-01")
    stock.addCoupon("CODE30", 30, "pain")
    assert stock.prix >= 0


def test_remise_appliquee_sur_article(stock):
    stock.ajouterArticle(50, "cerise", 2, "2023-01-01")
    stock.addCoupon("CODE2", 20, "cerise")
    assert stock.montantTotal == 80 