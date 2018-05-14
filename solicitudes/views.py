from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from rest_framework import generics, permissions
from rest_framework.generics import UpdateAPIView

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



class CreditRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CreditRequest.objects.all()
    serializer_class = CreditRequestSerializer

