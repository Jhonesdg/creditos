from rest_framework.serializers import ModelSerializer,ReadOnlyField,SerializerMethodField,RelatedField

from solicitudes.serializers import CreditRequestSerializer
from .models import Credit

class CreditSerializer(ModelSerializer):
    request = CreditRequestSerializer()
    manager_name = ReadOnlyField(source='manager.first_name')
    manager_lname = ReadOnlyField(source='manager.last_name')

    class Meta:
        model = Credit
        fields = ('id','installment_value','date','manager_name','manager_lname','request')

