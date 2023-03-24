from django.urls import path, include
from .views import CategoryListAPIView

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='category_list'),
]
