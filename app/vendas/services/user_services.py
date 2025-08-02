from vendas.models import UserModel
from django.core.exceptions import ValidationError

def marcar_como_vip(user_id):
    user = UserModel.objects.get(id=user_id)

    if not user:
        raise ValidationError("Usuário não existe")
    
    if user.vip:
        raise ValidationError("User já é vip")
    
    if "premium" not in user.adress.lower():
        raise ValidationError("Endereço não é de vip")
    
    user.vip = True
    user.save()
    return user