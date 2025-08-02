from rest_framework import viewsets
from vendas.models import Produto
from vendas.serializers.users_serializer import UsersSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = UsersSerializer
