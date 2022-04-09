"""Post URLs."""
from django.urls import path
from posts import views

urlpatterns = [
    path(
        route = '',
        view = views.PostListView.as_view(),
        name = 'feed'
        ),
    path(
        route='posts/new/',
        view = views.CreatePostView.as_view() ,
        name = 'new_post'
    ),

    path(
        route='posts/<int:pk>/',
        view = views.PostDetailView.as_view() ,
        name = 'detail'
    ),
]