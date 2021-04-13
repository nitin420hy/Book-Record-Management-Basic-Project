from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from BRM_app.forms import NewBookForm, SearchForm
from BRM_app import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('/BRM_app/view-books/')
        else:
            data['error']="username or password is incorrect"
            res=render(request,'BRM_app/user_login.html',data)
            return res
    else:
        return render(request,'BRM_app/user_login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRM_app/login')

@login_required(login_url="/BRM_app/login/")
def searchBook(request):
    form=SearchForm()
    res=render(request,'BRM_app/search_book.html',{'form':form})
    return res

@login_required(login_url="/BRM_app/login/")
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(Title=form.data['title'])
    res=render(request,'BRM_app/search_book.html',{'form':form,'books':books})
    return res

@login_required(login_url="/BRM_app/login/")
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRM_app/view-books')

@login_required(login_url="/BRM_app/login/")
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.Title,'price':book.Price,'author':book.Author,'Publisher':book.Publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRM_app/edit_book.html',{'form':form,'book':book})
    return res

@login_required(login_url="/BRM_app/login/")
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.Title=form.data['title']
        book.Price=form.data['price']
        book.Author=form.data['author']
        book.Publisher=form.data['publisher']
        book.save()
        return HttpResponseRedirect('BRM_app/view-books')

@login_required(login_url="/BRM_app/login/")
def viewBooks(request):
    books=models.Book.objects.all()
    username=request.session['username']
    res=render(request,'BRM_app/view_book.html',{'books':books,'username':username})
    return res

@login_required(login_url="/BRM_app/login/")
def newBook(request):
    form=NewBookForm()
    res=render(request,'BRM_app/new_book.html',{'form':form})
    return res

@login_required(login_url="/BRM_app/login/")
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
