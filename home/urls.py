from django.urls import path
from home.views import inicio, meu_logout

urlpatterns = [
    path('', inicio, name='inicio'),
    path('logout/', meu_logout, name="logout")
]
