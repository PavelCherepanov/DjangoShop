import requests
import json
from DjangoShop import settings
from .generateOrderId import generateOrderId 

class Qiwi:

    def __init__(self, request, amount):
        self.amount = amount
        self.order_id = generateOrderId(userId=request.user.id, amount=self.amount)

    def createInvoice(self):
        response = requests.get("https://oplata.qiwi.com/create?publicKey="+settings.QIWI_PUBLIK_KEY+"&amount="+str(self.amount)+"&successUrl=http%3A%2F%2F127.0.0.1%3Fthanks%3F&billId="+str(self.order_id))
        print(response.text)
        return response.url