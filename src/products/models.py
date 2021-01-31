from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    # => inheritance from the Model class

    title = models.CharField(max_length=120)  # maxlength is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    summary = models.TextField(blank=False, null=False)  # no blank => required
    featured = models.BooleanField(default=False)
    # field_name = models.FieldType(FieldValidationRequirements)

    def get_absolute_url(self):
        return reverse(
            "product-detail", kwargs={"id": self.id}
        )  # product-detail is how I named the URL for this view

    # Less dynamic method for abs URLs :
    # def get_absolute_url(self):
    #     return f"/products/{self.id}"


# Blank values for Django fields where blank=True
# (or filed types such as DateTimeField or ForeignKey)
# will be stored as NULL in the database.
