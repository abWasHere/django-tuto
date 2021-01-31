from django.shortcuts import render, get_object_or_404
from .models import Article


# def article_create_view(req):
#     article_detail_context = {"article": article}
#     render(req, "articles/article_create.html", article_detail_context)

def article_detail_view(req, art_id):
    article = get_object_or_404(Article, id=art_id)
    article_detail_context = {"article": article}
    return render(req, "articles/article_detail.html", article_detail_context)


def article_list_view(req):
    queryset = Article.objects.all()
    article_list_context = {"articles": queryset}
    return render(req, "articles/article_list.html", article_list_context)
