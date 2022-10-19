from dataclasses import fields
from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    """ Modèle de la serialisation d'un article """
    # comments = 
    class Meta:
        model = Article
        fields = ['url', 'title', 'image', 'category', 'overview', 'content', 'status', 'updated_on','created_on','author', 'comments']


