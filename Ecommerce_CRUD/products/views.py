from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import *
from products.models import Product

class productList(ListView):
    model = Product

class productView(DetailView):
    model = Product

class productCreate(CreateView):
    model = Product
    form_class = ProductForm
    
    success_url = reverse_lazy('product_list')

class productUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

class productDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')