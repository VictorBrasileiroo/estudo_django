from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from vendas.services.user_services import marcar_como_vip
from vendas.serializers.users_serializer import UsersSerializer

@api_view(['POST'])
def tornar_user_vip(request, user_id):
    try:
        user = marcar_como_vip(user_id)
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    except Exception as e:
        return Response({"erro" : str(e)}, status=status.HTTP_400_BAD_REQUEST)