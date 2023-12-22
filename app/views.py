from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.


def index(request):
    form = AddProduct.objects.all()
    return render(request, 'index.html', context={'form': form})


def create(request):
    if request.method == 'POST':

        form = AddProduct(request.POST)

        if form.is_valid():

            title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            price = form.cleaned_data['price']

            Products.objects.create(title=title, price=price)
    else:
        form = AddProduct()
        return render(request, 'index.html', context={'form': form})
