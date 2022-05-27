from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    """Serializer for the model object."""
    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at",)
        read_only_fields = ("id",)
