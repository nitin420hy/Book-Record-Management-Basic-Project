from django import forms

class NewBookForm(forms.form):
    title=forms.CharField(label='Title',max_length=100)
    price=forms.FloatField(label='Price')
    author=forms.CharField(label='Author',max_length=100)
    publisher=forms.CharField(label='Publisher',max_length=100)

class SearchForm(forms.form):
    title=forms.CharField(label='Title',max_length=100)
