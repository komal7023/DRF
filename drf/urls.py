from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from drf import views

router = DefaultRouter()
router.register(r"user", views.UserViewSet, basename="user")
router.register(r"", views.ProductViewSet)
router.register(r"", views.CategoryViewSet)
router.register(r"order", views.OrderViewSet, basename="order") 
router.register(r"cart", views.CartViewSet, basename="cart")


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]


