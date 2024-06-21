from django.urls import path
from . import views

urlpatterns = [
    path('singlepage/', views.singlepage, name='singlepage'),
]