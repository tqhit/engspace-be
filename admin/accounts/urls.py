from django.urls import path
from .views import *

urlpatterns = [
    path("", UserListAPIView.as_view()),
    path("<int:pk>/", UserDetailAPIView.as_view())
]
