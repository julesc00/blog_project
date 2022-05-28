from django.contrib.auth import get_user_model

from rest_framework.serializers import ModelSerializer

from .models import Post

User = get_user_model()


class PostSerializer(ModelSerializer):
    """Serializer for the model object."""
    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at",)
        read_only_fields = ("id",)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
        read_only_fields = ("id",)
