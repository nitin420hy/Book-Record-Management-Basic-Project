from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from BRM_app.forms import NewBookForm
from BRM_app import models

# Create your views here.
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id='bookid')
    book.delete()
    return HttpResponseRedirect('BRM_app/view-book')

def editBook(request):
    book=models.Book.object.get(id=request.GET['bookid'])
    fields={'title':book.Title,'price':book.Price,'author':book.Author,'Publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRM_app/edit_book.html',{'form':form,'book':book})
    return res

def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.Title=form.data['title']
        book.Price=form.data['price']
        book.Author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        return HttpResponseRedirect('BRM_app/view-book')

def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'BRM_app/view_book.html',{'books':books})
    return res

def newBook(request):
    form=NewBookForm()
    res=render(request,'BRM_app/new_book.html',{'form':form})
    return res

def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.Title=form.data['title']
        book.Price=form.data['price']
        book.Author=form.data['author']
        book.Publisher=form.data['publisher']
        book.save()
        s="Record Stored <br> <a href='/BRM_app/view-books'>View All Books</a>"
        return HttpResponse(s)
