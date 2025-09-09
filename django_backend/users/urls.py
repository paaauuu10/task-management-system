from django.urls import path
from .views import UserListView, UserDetailView, UserMeView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("me/", UserMeView.as_view(), name="user-me"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]