from datetime import datetime
import hashlib

timeDate = datetime.now() 

def generateOrderId(userId, amount):
    hashOrderId = hashlib.md5((str(userId)+str(timeDate)+str(amount)).encode())
    return hashOrderId.hexdigest()