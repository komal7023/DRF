from itertools import product
from django.urls import reverse
from rest_framework.test import APITestCase
from drf.models import Cart, Order, Product
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

class CategoryViewSetTest(APITestCase):
    def setUp(self):       
        User = get_user_model()
        self.user = User.objects.create_user(
            username='admin',
            password='man',
            email='admin@gmail.com'
        )
        self.client = APIClient()
        self.url = reverse('category-list')
        self.client.login(username='admin', password='man')
               
    def test_category_viewset(self):   
        data ={
            'name': 'mobile',
            'description': 'mobile',
        }       
        self.client.force_authenticate(self.user) 
        response = self.client.post(self.url, data, format='json') 
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)

class ProductViewSetTest(APITestCase):
    def setUp(self):      
        User = get_user_model()
        self.user = User.objects.create_user(
            username='admin',
            password='man',
            email='admin@gmail.com'
        )
        self.client = APIClient()
        self.url = reverse('product-list')
        self.client.login(username='admin', password='man')
               
    def test_product_viewset(self):   
        data ={
            'name': 'mobile',
            'description': 'mobile',
            'price': '12k',

        }       
        self.client.force_authenticate(self.user) 
        response = self.client.post(self.url, data, format='json') 
        print(response.data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_) 

class OrderViewSetTest(APITestCase):
    def setUp(self):
        
        User = get_user_model()
        self.user = User.objects.create_user(
            username='admin',
            password='man',
            email='admin@gmail.com'
        )
        self.client = APIClient()
        self.url = reverse('order-list')
        self.client.login(username='admin', password='man')
               
    def test_order_viewset(self):   
        product = Product(name="mobile")
        product.save()
        order = Order(product_name=product)
        order.save()

        record = Order.objects.get(id=1)
        self.assertEqual(record.product_name, "mobile")    
          
class CartViewSetTest(APITestCase):
    def setUp(self):
        
        User = get_user_model()
        self.user = User.objects.create_user(
            username='admin',
            password='man',
            email='admin@gmail.com'
        )
        self.client = APIClient()
        self.url = reverse('cart-list')
        self.client.login(username='admin', password='man')
               
    def test_cart_viewset(self):   
        user = get_user_model()(username = "adminnn")
        user.save()
        product = Product(name = "ship")
        product.save()
        order = Cart(user=user, product=product)
        order.save()

        record = Cart.objects.get(id=1)
        self.assertEqual(record.product.name, 'ship') 