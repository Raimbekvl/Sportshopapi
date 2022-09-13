from django import forms

from product.models import Document
# from product.models import Product


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )