from django.db.models.base import Model
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = "__all__"