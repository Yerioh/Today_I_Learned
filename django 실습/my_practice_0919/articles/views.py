# import random
from django.shortcuts import render
import random


# Create your views here.
def index(request):
    if request.GET:
        user_id = request.GET.get('user-id')
        context = {
            'name' : user_id,
        }
        return render(request, 'articles/index.html', context)
    context = {
        'name' : '사용자',
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)


def login(request):
    return render(request, 'articles/login.html')