from django.shortcuts import render
from .models import Product_model

# Create your views here.
def hello_world(request):
    context={'product': Product_model.objects.all()}
    return render(request, 'shop/home.html', context=context)
