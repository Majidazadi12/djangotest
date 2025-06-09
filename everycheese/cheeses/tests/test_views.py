import pytest
from pytest_django.asserts import(
    assertContains,assertRedirects
)
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory
from everycheese.users.models import User
from everycheese.cheeses.models import Cheese
from everycheese.cheeses.views import CheeseCreateView,CheeseListView,CheeseDetailView,CheeseUpdateView
from everycheese.cheeses.tests.factories import CheeseFactory
from everycheese.cheeses.tests.factories import cheese
pytestmark=pytest.mark.django_db

def test_good_cheese_list_view(rf):
    request=rf.get(reverse("cheeses:list"))
    response=CheeseListView.as_view()(request)
    assertContains(response,'Cheese List')
def test_good_cheese_detail_view(rf,cheese):
    url=reverse("cheeses:detail",kwargs={'slug':cheese.slug})
    request=rf.get(url)
    callable_obj=CheeseDetailView.as_view()
    response=callable_obj(request,slug=cheese.slug)
    assertContains(response,cheese.name) 
def test_good_cheese_create_view(rf,admin_user,cheese):
    request=rf.get(reverse("cheeses:add"))
    request.user=admin_user
    response=CheeseCreateView.as_view()(request)
    assert response.status_code==200 
def test_homepage_view():
    template_name='index.html'
    assert template_name=='index.html' 
def test_form_valid():
    assert 1==1
def test_cheese_create_form_valid(rf,admin_user):
    form_data={
        "name":"Paski Sir",
        "description":"A salty hard cheese",
        "firmness":Cheese.Firmness.HARD
        
    }
    request=rf.post(reverse("cheeses:add"),form_data)
    request.user=admin_user
    response=CheeseCreateView.as_view()(request)
    cheese=Cheese.objects.get(name="Paski Sir")
    assert cheese.description=="A salty hard cheese"
    assert cheese.firmness==Cheese.Firmness.HARD
    assert cheese.creator==admin_user     
def test_cheese_list_contains_2_cheeses(rf):
    cheese1=CheeseFactory()
    cheese2=CheeseFactory()
    request=rf.get(reverse('cheeses:list'))
    response=CheeseListView.as_view()(request)  
    assertContains(response,cheese1)
    assertContains(response,cheese2)
def test_detail_contains_cheese_data(rf,cheese):
    url=reverse("cheeses:detail",kwargs={'slug':cheese.slug})
    request=rf.get(url)                   
    callable_obj=CheeseDetailView.as_view()
    response=callable_obj(request,slug=cheese.slug)
    assertContains(response,cheese.name)
    assertContains(response,cheese.get_firmness_display())
    assertContains(response,cheese.country_of_origin)
def test_cheese_create_correct_title(rf,admin_user):
    request=rf.get(reverse('cheeses:add'))
    request.user=admin_user
    response=CheeseCreateView.as_view()(request)
    assertContains(response,'Add Cheese')    
 
def test_good_cheese_update_view(rf,admin_user,cheese):
    url=reverse("cheeses:update",kwargs={'slug':cheese.slug})
    request=rf.get(url)
    request.user=admin_user
    callable_obj=CheeseUpdateView.as_view()
    response=callable_obj(request,slug=cheese.slug)
    assertContains(response,"Update Cheese")
def test_cheese_update(rf,admin_user,cheese):
    form_data={
        'name':cheese.name,
        'description':'Something new',
        'firmness':cheese.firmness
    }
    url=reverse("cheeses:update",kwargs={'slug':cheese.slug})
    request=rf.post(url,form_data)  
    request.user=admin_user
    callable_obj=CheeseUpdateView.as_view()
    response=callable_obj(request,slug=cheese.slug)
    cheese.refresh_from_db()
    assert cheese.description=='Something new'
     