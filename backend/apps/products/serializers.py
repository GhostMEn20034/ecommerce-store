from rest_framework import serializers
from .models import Category
from services.cached_category_tree import CachedCategories


class CategorySerializer(serializers.ModelSerializer):

    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'children', )

    def get_children(self, obj):
        cached_categories = CachedCategories.get_instance()
        children = cached_categories.get_children(obj)
        return CategorySerializer(children, many=True).data
