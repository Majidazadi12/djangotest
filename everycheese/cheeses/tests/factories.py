from django.template.defaultfilters import slugify
from everycheese.users.tests.factories import UserFactory
import factory
import factory.fuzzy
import pytest
@pytest.fixture
def cheese():
    return CheeseFactory()
from everycheese.cheeses.models import Cheese

class CheeseFactory(factory.django.DjangoModelFactory):
    name=factory.fuzzy.FuzzyText()
    slug=factory.LazyAttribute(lambda obj:slugify(obj.name))
    description=factory.Faker('paragraph',nb_sentences=6
                            
                              )
    firmness=factory.fuzzy.FuzzyChoice(
        [x[0] for x in Cheese.Firmness.choices]
    )
    country_of_origin=factory.Faker('country_code')
    creator=factory.SubFactory(UserFactory)
    class Meta:
        model=Cheese