# from django.conf import settings
# from management.models import Product
from DjangoShop import settings
from management.models import Product
from decimal import Decimal

class Cart(object):

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, productId, quantity=1, update_quantity=False):
        product = Product.objects.get(id=productId)
        productId = str(product.id)
        if productId not in self.cart:
            self.cart[productId] = {'img':str(product.product_img), 'quantity':0, 'price':str(product.product_price)}

        if update_quantity:
            self.cart[productId]['quantity'] = quantity
        else:
            self.cart[productId]['quantity'] += quantity
        self.save()        

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

        # def get_total_price(self):
        # """
        # Подсчет стоимости товаров в корзине.
        # """
        # return sum(Decimal(item['price']) * item['quantity'] for item in
        #         self.cart.values())