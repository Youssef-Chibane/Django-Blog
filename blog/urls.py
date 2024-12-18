from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('posts', views.posts, name='posts'),
    path('post_detail', views.post_detail, name='post_detail'),
]
