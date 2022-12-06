from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:slug>', views.selected_post, name='selected_post'),
]
