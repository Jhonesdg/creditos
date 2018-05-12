from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import parsers, renderers, permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from usuarios.serializers import CustomLoginSerializer,ClientRegisterSerializer
from .models import Client
from rest_framework.generics import CreateAPIView

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CustomLoginSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        context = {}
        user = serializer.validated_data['user']
        user_data = {
            'id': user.id,
            'nombre': user.first_name,
            'apellido': user.last_name,
        }
        context['user'] = user_data

        return Response(context, content_type='application/json')



class ClientRegister(CreateAPIView):
    serializer_class = ClientRegisterSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

