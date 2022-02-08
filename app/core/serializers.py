from rest_framework import serializers
from core.models import exchange_modal


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = exchange_modal
        fields = ['current_price', 'last_refreshed']


