from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "author"]

    def clean_title(self):
        data = self.cleaned_data.get("title")
        if "fuck" in data:
            raise "Swear words are forbidden !"
        return data
