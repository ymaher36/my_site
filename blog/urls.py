from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_posts/', views.all_posts, name='all-posts'),
    path('post/<slug:slug>', views.selected_post, name='selected_post'),
]
