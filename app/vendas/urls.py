from rest_framework.routers import DefaultRouter
from django.urls import path
from vendas.views.users_custom_view import tornar_user_vip
from vendas.views.users_view import UserViewSet

router = DefaultRouter()
router.register(r'usuarios', UserViewSet)

urlpatterns = [
    *router.urls,
    path('usuarios/<int:user_id>/tornar-vip/', tornar_user_vip),
]
