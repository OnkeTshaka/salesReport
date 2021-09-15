from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    product = Product.objects.all()
    context={'product':product}
    return render(request,'index.html',context)


def create(request):
    return render(request,'products/form.html')


def edit(request,pk):
    return render(request,'products/form.html')


def remove(request):
    return render(request,'products/delete.html')


def details(request,pk):
    return render(request,'products/detail.html')