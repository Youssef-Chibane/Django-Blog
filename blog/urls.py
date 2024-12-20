from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name="logout"),
    path('posts', views.posts, name='posts'),
    path('post_detail/<int:pk>', views.post_detail, name='post_detail'),
    path('create_post', views.create_post, name='create_post'),
    path('update_post/<int:pk>', views.update_post, name='update_post'),
]
