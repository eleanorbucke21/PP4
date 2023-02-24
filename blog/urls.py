from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.Likes.as_view(), name='likes'),
    path('dislike/<slug:slug>', views.Dislikes.as_view(), name='dislikes'),
    path('post/edit/<slug:slug>/', views.EditPost.as_view(), name='update_post'),
    path('delete/<slug:slug>/remove', views.DeletePost.as_view(), name='delete_post'),
]
