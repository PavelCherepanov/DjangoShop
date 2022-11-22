import requests
import json
from DjangoShop import settings

class CryptoCloud():

    def __init__(self, amount, order_id):
        self.amount = amount
        self.order_id = order_id

    def createInvoice(self):
        result = requests.post('https://api.cryptocloud.plus/v1/invoice/create',
        headers={"Authorization": "Token "+ settings.CRYPTO_CLOUD_TOKEN},
        data={"amount":str(self.amount), "shop_id":settings.CRYPTO_CLOUD_SHOP_ID,"currency":"USD",
        "order_id":str(self.order_id)})
        response = json.loads(result.text)
        return response["pay_url"]

 