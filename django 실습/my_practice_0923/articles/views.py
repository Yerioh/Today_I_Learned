from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = list(Article.objects.all())
    articles.sort(key=lambda x: x.pk, reverse=True)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create_view(request):
    return render(request, 'articles/create_view.html')

def create_article(request):
    Article.objects.create(
        title = request.GET.get('title'),
        content = request.GET.get('content'),
    )
    return redirect('articles:index')

def detail(request, id):
    data = Article.objects.get(pk=id)
    context = {
        'article': data,
    }
    return render(request, 'articles/detail.html', context)

def delete(request):
    id = request.GET.get('id')
    article = Article.objects.get(pk=id)
    article.delete()
    return redirect('articles:index')