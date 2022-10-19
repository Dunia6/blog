from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """ Modèle catégorie d'un article  """
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


CHOIX_STATUS = (
    ("brouillon", "Brouillons"),
    ("publié", "Publié"),
)
class Article(models.Model):
    """ Modèle de l'article du bloc """
    title = models.CharField(max_length=100, blank=True, unique=True)
    slug = models.SlugField(max_length=200,blank=True, unique=True)
    image = models.ImageField(upload_to="uploads/images/{0}",null=True, blank='True')
    category = models.ForeignKey(Category, blank=True,on_delete=models.CASCADE, related_name='articles')
    overview = models.TextField()
    content = models.TextField()
    status = models.CharField(choices=CHOIX_STATUS, max_length=200, default="brouillon")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title



class Comment(models.Model):
    """ Modèle Commentaire """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return "Commentaire {}, commenté par {}".format(self.body, self.name)
