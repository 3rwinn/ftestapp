from rest_framework import serializers
from .models import Transfert

class TransfertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfert
        fields = "__all__"