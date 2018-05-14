from rest_framework import generics

from .serializers import CreditSerializer
from .models import Credit

# Create your views here.
class CreditUserList(generics.ListAPIView):
    model = Credit
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

    def get_queryset(self):
        queryset = super(CreditUserList, self).get_queryset()
        return queryset.filter(request__client__pk=self.kwargs.get('pk'))