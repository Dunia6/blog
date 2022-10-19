from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.HyperlinkedRelatedField):
    """ Modèle de la serialisation d'un commentaire """

    class Meta:
        model = Comment
        fields = ['url', 'name', 'email', 'body', 'active']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    """ Modèle de la serialisation d'un article """
    # comments = serializers.HyperlinkedRelatedField(many=True, view_name='comments_view')

    class Meta:
        model = Article
        fields = ['url', 'title', 'image', 'category', 'overview', 'content', 'status', 'updated_on','created_on','author']