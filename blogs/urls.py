from django.urls import path
from .views import Blogs,Post,CreatePost,UpdatePost,DeletePost

urlpatterns = [
    path('',Blogs.as_view(),name='blogs'),
    path('add/',CreatePost.as_view(),name='post-create'),
    path('update/<int:pk>/',UpdatePost.as_view(),name='post-update'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='post-delete'),
    path('<int:pk>/',Post.as_view(),name='post-detail'),
]
