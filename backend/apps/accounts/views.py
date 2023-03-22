from rest_framework import generics
from .serializers import CustomerSerializer
from .models import Customer


class AccountDetail(generics.RetrieveAPIView):
    queryset = Customer.objects.all().select_related('user').prefetch_related('addresses')
    serializer_class = CustomerSerializer
    lookup_field = 'user'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(user=self.request.user.id)
        # obj = queryset.get(user=4)
        return obj
