from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        # parser_classes = [FormParser, MultiPartParser]

class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        # parser_classes = [FormParser, MultiPartParser]