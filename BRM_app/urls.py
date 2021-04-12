from django.conf.urls import url, include
from BRM_app import views

urlpatterns = [
    url('view-books',views.viewBooks),
    url('edit-book',views.editBook),
    url('delete-book',views.deleteBook),
    url('search-book',views.searchBook),
    url('new-book',views.newBook),
    url(r'^add',views.add),
    url('search',views.search),
    url('edit',views.edit),
]
