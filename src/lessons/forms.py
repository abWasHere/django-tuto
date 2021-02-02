from django import forms
from .models import Lesson


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "teacher"]

    def clean_teacher(self):
        data = self.cleaned_data.get("teacher")
        if "toto" in data:
            raise forms.ValidationError("No toto allowed !")
        return data


    def clean_title(self):
        data = self.cleaned_data["title"]
        if data.lower() == "abc":
            raise forms.ValidationError("abc is not a valid title !")
        return data
