from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Article
from .forms import ArticleForm as ArticleModelForm


# CLASS BASED VIEWS != function based views

class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    # template has to be formatted like <blog>/<modelname>_list.html ?
    queryset = Article.objects.all()
    # the context is now an "object_list"


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    queryset = Article.objects.all()  # the context is now an "object"

    # if we let "id" as the request param in the URLs :
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    queryset = Article.objects.all()
    form_class = ArticleModelForm


class ArticleUpdateView(UpdateView):
    template_name = "articles/article_create.html"
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse("articles:article-list")
