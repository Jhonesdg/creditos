from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, permissions
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

