from rest_framework.routers import DefaultRouter
from vendas.views.users_view import UserViewSet

router = DefaultRouter()
router.register(r'usuarios', UserViewSet)

urlpatterns = router.urls
