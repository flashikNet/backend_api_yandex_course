import requests

BASE_URL = 'https://fakestoreapi.com'

products = requests.get(f'{BASE_URL}/products').json()
products_less_twenty = filter(lambda x: x['price'] < 20, products)

categories = requests.get(f'{BASE_URL}/products/categories').json()
jewelery_products = requests.get(f'{BASE_URL}/products/category/jewelery').json()

users = requests.get(f'{BASE_URL}/users').json()

my_user = {  # user with my name
    'email': 'Evgeniy@gmail.com',
    'username': 'Evgeniy',
    'password': 'm38rmF$',
    'name': {
        'firstname': 'Evgeniy',
        'lastname': 'Doe'
    },
    'address': {
        'city': 'kilcoole',
        'street': '7835 new road',
        'number': 3,
        'zipcode': '12926-3874',
        'geolocation': {
            'lat': '-37.3159',
            'long': '81.1496'
        }
    },
    'phone': '1-570-236-7033'
}
my_user_response = requests.post(f'{BASE_URL}/users', json=my_user).json()

print(*products_less_twenty)
print(categories)
print(jewelery_products)
print(users)
print(my_user_response)

# TODO:
#
# REST API Fake Store - https://fakestoreapi.com/
#
# Самостоятельно:
# 1 Вывести продукты, цена которых <20
# 2 Вывести все категории
# 3 Вывести все продукты с категорией  "jewelery"
# 4 Вывести всех пользователей
# 5 Добавить пользователя со своим именем.
