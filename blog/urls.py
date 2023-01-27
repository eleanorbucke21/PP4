from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.Likes.as_view(), name='likes'),
    path('dislike/<slug:slug>', views.Dislikes.as_view(), name='dislikes'),
]