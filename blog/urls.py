from django.urls import path

from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('all_posts/', views.AllPostsView.as_view(), name='all-posts'),
    path('post/<slug:slug>', views.SelectedPostView.as_view(), name='selected_post'),
]
