from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]



