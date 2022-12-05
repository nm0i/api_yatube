from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ("id", "text", "author", "image", "pub_date")
        read_only_fields = ("author",)
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "slug", "description", "title")
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ("id", "author", "post", "created", "text")
        read_only_fields = (
            "author",
            "post",
        )
        model = Comment
