from django import forms
from .models import Book


class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'author': 'Autor',
            'category': 'Categoria',
            'description': 'Descrição',
            'release_date': 'Data de lançamento',
            'user_id': 'Usuário',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'release_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),
            'user_id': forms.Select(attrs={'class': 'form-control'}),
        }
