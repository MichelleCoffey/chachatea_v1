from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='blog'),
    path('<slug:slug>/', views.blog_details, name='blog_details')
]



