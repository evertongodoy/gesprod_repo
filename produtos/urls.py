from django.urls import path
from produtos.views import prod_list
from produtos.views import prod_new
from produtos.views import prod_upd
from produtos.views import prod_del

urlpatterns = [
    path('list/', prod_list, name='prod_list'),
    path('new/', prod_new, name='prod_new'),
    path('update/<int:id>', prod_upd, name='prod_upd'),
    path('delete/<int:id>', prod_del, name='prod_del'),
]
