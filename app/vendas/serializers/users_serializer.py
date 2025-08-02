from rest_framework import serializers
from vendas.models import UserModel

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
