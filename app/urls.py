from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    # path('product/', product, name='product'),
    path('create/', create, name='create'),
]