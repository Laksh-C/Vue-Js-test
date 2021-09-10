from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from .models import testmodel
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import ProductCreateForm
from django.urls import reverse_lazy

# Create your views here.

    

def homepage(request):
    return render(request, 'home.html')

class buyerpage(ListView):
    model = testmodel
    template_name = "buyer.html"

class sellerpage(CreateView):
    form_class = ProductCreateForm
    template_name = "seller.html"
    success_url = reverse_lazy("buyer")
