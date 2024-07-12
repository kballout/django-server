from django.urls import re_path as  url
from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView
)

urlpatterns = [
    path('api', PostListView.as_view()),
    path('api/<int:post_id>/', PostDetailView.as_view()),
]