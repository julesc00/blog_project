from django.urls import path

from .views import PostList, PostDetail

app_name = "posts"

urlpatterns = [
    path("", PostList.as_view(), name="list-posts"),
    path("<int:pk>/", PostDetail.as_view(), name="detail-post"),
]
