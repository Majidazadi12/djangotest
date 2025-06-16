from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView
from .models import Cheese



from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
class HomepageView(TemplateView):
    template_name='index.html'
class CheeseListView(ListView):
       model = Cheese

class CheeseDetailView(DetailView):
      model=Cheese
class CheeseCreateView(PermissionRequiredMixin,LoginRequiredMixin,CreateView):
    model=Cheese
    fields=['name','description','firmness','country_of_origin']
    def form_valid(self, form):
        form.instance.creator=self.request.user
        return super().form_valid(form)
    permission_required = "cheeses.add_cheese"

class CheeseUpdateView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model=Cheese
    fields=[
        'name',
        'description',
        'firmness',
        'country_of_origin'
    ]
    permission_required = "cheeses.change_cheese"
    action="Update"    