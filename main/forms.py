from .models import Prod
from django.forms import ModelForm, TextInput, Textarea


class ProdForm(ModelForm):
    class Meta:
        model = Prod
        fields = ["prod_name", "prod_price", "prod_task"]
        widgets = {
            "prod_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование товара'
            }),
            "prod_price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену товара'
            }),
            "prod_task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание товара'
            }),
        }