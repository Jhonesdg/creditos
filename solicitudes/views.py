
from django.http import  QueryDict
from django.views.generic import TemplateView
from rest_framework import generics, permissions
from rest_framework.utils import json

from credits.models import Credit
from usuarios.models import Manager
from .serializers import CreditRequestSerializer
from .models import CreditRequest
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class CreditRequestList(generics.ListCreateAPIView):
    model = CreditRequest
    queryset = CreditRequest.objects.all()
    serializer_class = CreditRequestSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CreditRequestUserList(generics.ListAPIView):
    model = CreditRequest
    queryset = CreditRequest.objects.all()
    serializer_class = CreditRequestSerializer

    def get_queryset(self):
        queryset = super(CreditRequestUserList, self).get_queryset()
        return queryset.filter(client__pk=self.kwargs.get('pk'))

class CreditRequestManagerList(generics.ListAPIView):
    model = CreditRequest
    queryset = CreditRequest.objects.all()
    serializer_class = CreditRequestSerializer

    def get_queryset(self):
        queryset = super(CreditRequestManagerList, self).get_queryset()
        return queryset.filter(status=1)



class CreditRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditRequest.objects.all()
    serializer_class = CreditRequestSerializer
    lookup_field = 'pk'
    def put(self, request, *args, **kwargs):
        print(self)

        instance = self.get_object()
        put_params=QueryDict(request.body)

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        if body['status']==2:
            ivalue=(float(instance.amount)/float(instance.installments))+(float(instance.type.rate)*float(instance.amount))
            Credit.objects.create(installment_value=ivalue,manager=Manager.objects.get(username=body['manager']),
                                  request=instance,)


        return self.update(request, *args, **kwargs)
