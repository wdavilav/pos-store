import json
import os
import random
import string
from datetime import date

import django

from config import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.pos.models import Product, Category, Client, SaleDetail, Sale, Company


def insert_data():
    numbers = list(string.digits)

    company = Company()
    company.name = 'POS-STORE S.A.'
    company.ruc = '0928363993001'
    company.address = 'MILAGRO, CDLA PAQUISHA'
    company.mobile = '0996555528'
    company.phone = '2977557'
    company.email = 'williamjair94@hotmail.com'
    company.website = 'https://algorisoft.com'
    company.description = 'VENTA AL POR MAYOR Y MENOS DE PRODUCTOS DE PRIMERA NECESIDAD'
    company.iva = 12.00
    company.save()

    with open(f'{settings.BASE_DIR}/deploy/json/products.json', encoding='utf8') as json_file:
        for item in json.load(json_file):
            product = Product()
            product.name = item['name']
            product.code = item['code']
            product.category = Category.objects.get_or_create(name=item['category'])[0]
            product.price = float(item['price'])
            product.pvp = float(item['pvp'])
            product.stock = random.randint(50, 150)
            product.save()
            print(f'record inserted product {product.id}')

    category = Category.objects.create(name='SERVICIOS')
    Product(name='FORMATEO DE COMPUTADORAS', category=category, is_service=True, with_tax=False, pvp=15.00, code='FORMATEO85451').save()

    client = Client()
    client.names = 'Consumidor Final'
    client.dni = '9999999999999'
    client.email = 'davilawilliam94@gmail.com'
    client.birthdate = date(1994, 10, 19)
    client.mobile = '9999999999'
    client.address = 'Milagro, cdla. Paquisha'
    client.save()

    with open(f'{settings.BASE_DIR}/deploy/json/customers.json', encoding='utf8') as json_file:
        data = json.load(json_file)
        for item in data[0:20]:
            client = Client()
            client.names = f"{item['first']} {item['last']}"
            client.dni = ''.join(random.choices(numbers, k=10))
            client.birthdate = date(random.randint(1969, 2006), random.randint(1, 12), random.randint(1, 28))
            client.mobile = ''.join(random.choices(numbers, k=10))
            client.email = item['email']
            client.address = item['country']
            client.save()
            print(f'record inserted client {client.id}')

    client_id = list(Client.objects.filter().values_list('id', flat=True))
    for i in range(1, random.randint(6, 10)):
        sale = Sale()
        sale.company_id = 1
        sale.employee_id = 1
        sale.client_id = random.choice(client_id)
        sale.iva = 0.12
        sale.save()
        print(f'record inserted sale {sale.id}')
        for d in range(1, 8):
            list_products = list(Product.objects.filter(stock__gt=0).values_list(flat=True))
            if len(list_products):
                detail = SaleDetail()
                detail.sale_id = sale.id
                detail.product_id = random.choice(list_products)
                detail.cant = random.randint(1, int((detail.product.stock * 0.30)))
                detail.price = detail.product.pvp
                detail.save()
                detail.product.stock -= detail.cant
                detail.product.save()
        sale.calculate_detail()
        sale.calculate_invoice()
        sale.cash = sale.total
        sale.save()


insert_data()
