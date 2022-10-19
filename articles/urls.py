from .views import ArticleViews
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"articles", ArticleViews, basename='articles')



urlpatterns = [
    path('api/', include(router.urls)),
    # path('articleDetail/<str:slug>/', ArticleDetail.as_view(),),
]

urlpatterns += format_suffix_patterns(urlpatterns)