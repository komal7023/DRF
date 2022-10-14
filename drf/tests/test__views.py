from django.urls import reverse
from rest_framework.test import APITestCase
from drf.models import Category, Product
from rest_framework.test import APIClient
from http import HTTPStatus
from django.contrib.auth import get_user_model
from rest_framework.test import force_authenticate 


class UserViewSetTest(APITestCase):
    def setUp(self):        
        User = get_user_model()
        self.user = User.objects.create_user(
            username='admin',
            password='man',
            email='admin@gmail.com'
        )
        self.url = reverse('user')
        print('test user:' + str(self.user))

    def test_user_viewset(self):
        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'somepassword'
        }
        client = APIClient()
        client.force_authenticate(self.user)
        response = client.post(self.url, data)
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)

# class ProductViewSetTest(APITestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create_user(
#             username='admin',
#             password='man',
#             email='admin@gmail.com'
#         )
#         self.url = reverse('product-list')
               
#     def test_product_viewset(self):
#         self.products = Product.objects.all()
#         client = APIClient()      
#         client.force_authenticate(self.user) 
#         response = client.get(self.url, format='json') 
#         self.assertEqual(response.status_code, HTTPStatus.OK._value_)
        