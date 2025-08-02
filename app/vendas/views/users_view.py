from rest_framework import viewsets
from vendas.models import UserModel
from vendas.serializers.users_serializer import UsersSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UsersSerializer
