from django import forms
from myNewWeb.models import Produk
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''