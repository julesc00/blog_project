from django.urls import path

from .views import PostList, PostDetail, UserListView, UserDetailView

app_name = "posts"

urlpatterns = [
    path("", PostList.as_view(), name="list-posts"),
    path("<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("users/", UserListView.as_view(), name="list-users"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
