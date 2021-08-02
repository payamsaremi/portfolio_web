from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, PostViewSet

router = DefaultRouter()
router.register(r'projects', PostViewSet, basename="posts")
router.register(r'categories', CategoryViewSet, basename="categories")

urlpatterns = [
    path('', include(router.urls))
]