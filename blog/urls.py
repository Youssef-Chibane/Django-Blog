from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name="logout"),
    path('posts', views.posts, name='posts'),
    path('post/create', views.create_post, name='create'),
    path('post/<int:pk>/detail', views.post_detail, name='detail'),
    path('post/<int:pk>/update', views.update_post, name='update'),
    path('post/<int:pk>/delete', views.delete_post, name='delete'),
]
