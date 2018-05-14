from rest_framework.serializers import ModelSerializer,ReadOnlyField,SerializerMethodField,DateField

from .models import CreditRequest,TypeCredit


class CreditRequestSerializer(ModelSerializer):
    status = SerializerMethodField()
    type_name = ReadOnlyField(source='type.name')
    client_name = ReadOnlyField(source='client.first_name')
    client_lname = ReadOnlyField(source='client.last_name')
    class Meta:
        model = CreditRequest
        fields = ('id','client','client_name','client_lname','amount','type_name','installments','description','status','date','type','observations')

    def get_status(self, obj):
        return obj.get_status_display()
