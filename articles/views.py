from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from articles.serializers import ArticleSerializer
from .models import Article

# Create your views here.


class ArticleViews(ReadOnlyModelViewSet):
    """ Vue pour afficher la liste des articles """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    



# class ArticleDetail():
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer