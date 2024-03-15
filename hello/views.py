from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from hello.models import Article

def index(request):
  articles =Article.objects.filter(pk__in=[1,3])
  context={
    "articles":articles,
  }
  return render(request,"hello/index.html",context)

class IndexView(generic.ListView):
  model=Article
  template_name="hello/index2.html"