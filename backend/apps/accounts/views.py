from rest_framework import generics, response
from .serializers import CustomerSerializer
from .models import Customer
from .permissions import IsAuthenticatedAndOwner


class AccountDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedAndOwner, ]
    queryset = Customer.objects.all().select_related('user').prefetch_related('addresses')
    serializer_class = CustomerSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(user=self.request.user.id)
        print(self.request.data)
        return obj
