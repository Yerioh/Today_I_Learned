from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('login/', views.login, name='login'),
]
