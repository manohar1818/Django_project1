from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q

# Create your views here.
from .models import Article

def index(request):
    return render(request,'firstpage.html')


def hard(request,iid):
    all_article = Article.objects.filter(id = iid)
    if all_article:
        contet = {
            'all_article': all_article
        }
        return render(request,'backpage.html',contet)
    else:
        return HttpResponseNotFound("Article not found")



def all_news(request):
    all_articles = Article.objects.all()
    if all_articles:
        context = {
            'all_articles': all_articles
        }
        return render(request, 'frontpage.html', context)
    else:
        return HttpResponseNotFound("Article not found")
