from rest_framework import generics
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from services.cached_category_tree import CachedCategories


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.published.all()

    def get(self, request, *args, **kwargs):
        categories = self.get_queryset()
        cached_categories = CachedCategories(categories).get_cached_root_nodes()
        serializer = self.serializer_class(cached_categories, many=True)
        return Response(serializer.data)
