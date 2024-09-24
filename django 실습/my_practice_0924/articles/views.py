from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    # 게시글은 보통 역순으로 보이므로 재정렬
    articles = sorted(list(articles), key=lambda x: x.pk, reverse=True)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title = title, content = content)
    article.save()
    return redirect('articles:detail', article.pk)

def delete(request):
    pk = request.POST.get('pk')
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request):
    pk = request.POST.get('pk')
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', pk)