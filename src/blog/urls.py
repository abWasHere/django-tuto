from django.urls import path
from .views import article_list_view, article_detail_view

urlpatterns = [
    path("", article_list_view, name="article-list"),
    path("article/<int:art_id>", article_detail_view, name="article-detail"),
]
