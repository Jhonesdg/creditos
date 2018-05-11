from rest_framework.serializers import ModelSerializer

from .models import CreditRequest


class CreditRequestSerializer(ModelSerializer):
    class Meta:
        model = CreditRequest
        fields = '__all__'
