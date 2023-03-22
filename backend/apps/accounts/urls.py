from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import AccountDetail

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Gives access and refresh tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh the access token
    path('personal-information/', AccountDetail.as_view(), name='personal_info'),
]
