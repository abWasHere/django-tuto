from django import forms
from .models import Product

# Those objects will take the form data as parameters (cf. views.py) and apply the field validations


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price"]

    def clean_title(self):
        data = self.cleaned_data.get("title")
        if "X" in data:
            raise forms.ValidationError("No X allowed in title !")
        if "yo" not in data:
            raise forms.ValidationError("Not a valid title. Add 'yo' !")
        return data


# Form based on customed validation fields edited here :
class RawProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(
        required=False,
        label="",
        widget=forms.Textarea(attrs={"rows": 20, "cols": 100}),
    )
    price = forms.DecimalField(initial=10)
