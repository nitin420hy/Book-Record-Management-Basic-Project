from django.shortcuts import render
from django.http import HttpResponse
from BRM_app.forms import NewBookForm
from BRM_app.models import Book

# Create your views here.
def newBook(request):
    form=NewBookForm()
    res=render(request,'BRM_app/new_book.html',{'form':form})
    return res
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=Book()
        book.Title=form.data['title']
        book.Price=form.data['price']
        book.Author=form.data['author']
        book.Publisher=form.data['publisher']
        book.save()
        s="Record Stored <br> <a href='/BRM_app/view-books'>View All Books</a>"
        return HttpResponse(s)
