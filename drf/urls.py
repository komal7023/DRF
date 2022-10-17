from unicodedata import name
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from drf import views

router = DefaultRouter()
router.register(r"product", views.ProductViewSet, basename='product')
router.register(r"category", views.CategoryViewSet, basename='category')
router.register(r"order", views.OrderViewSet, basename='order') 
router.register(r"cart", views.CartViewSet, basename='cart')

urlpatterns = [
    path('user/',views.UserViewSet.as_view({'get': 'list'}), name='user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]

