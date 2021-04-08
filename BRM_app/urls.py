from django.conf.urls import url, include
from BRM_app import views

urlpatterns = [
    url('view-books',views.viewBooks)
]
