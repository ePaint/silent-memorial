from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_id', 'create_date', 'author', 'title', 'content', 'birth_date', 'death_date', 'is_public')
        read_only_fields = ('post_id', 'create_date')
