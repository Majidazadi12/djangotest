import pytest

from everycheese.cheeses.tests.factories import CheeseFactory

pytestmark=pytest.mark.django_db

def test___str__():
    cheese=CheeseFactory()
    assert cheese.__str__()==cheese.name
    assert str(cheese)==cheese.name
    
def test_get_absolute_url():
    cheese=CheeseFactory()
    url=cheese.get_absolute_url()
    assert url==f'/cheeses/{cheese.slug}/'
       