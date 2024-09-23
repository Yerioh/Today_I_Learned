from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_view, name='create'),
    path('create_article/', views.create_article, name='create_article'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('delete/', views.delete, name='delete')
]