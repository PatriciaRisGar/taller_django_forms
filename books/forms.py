
from typing import Any
from django import forms
from django.contrib.auth.models import User
from books.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'rating')

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if  author.username == 'admin':
            raise forms.ValidationError ('The author cannot be admin')
        
        return author