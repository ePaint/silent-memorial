import os

from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from .models import Post


# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
