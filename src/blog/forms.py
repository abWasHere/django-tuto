from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "author", "active"]

    def clean_author(self):
        data = self.cleaned_data.get("author")
        if "toto" in data:
            raise forms.ValidationError("No toto allowed !")
        return data
