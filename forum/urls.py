from django.urls import path
from .views import *

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailAPIView.as_view(), name="post_detail")
]
