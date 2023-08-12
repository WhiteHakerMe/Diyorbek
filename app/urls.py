from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home_uy"),
    path('portfolio/<slug>', views.Portfolios, name='Portfolio_pot')
]