from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
  # 获取models中的数据
  article = models.Article.objects.get(pk=1)
  print(article.title)
  return render(request, 'index.html', {'article': article})