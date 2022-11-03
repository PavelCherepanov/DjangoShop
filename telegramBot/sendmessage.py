import requests
from .models import TelegramSettings


def sendCrmTelegram(tg_name, tg_email):
    if TelegramSettings.objects.get(pk=1):
        settings = TelegramSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = "https://api.telegram.org/bot"+token+"/sendMessage"
        text = text+": " + tg_name + "\n" + tg_email
        try:
            req = requests.post(api, data={
                'chat_id':chat_id,
                'text':text
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print("Error")
            elif req.status_code == 500:
                print("Server Error")
            else:
                print("Success")

    else:
        pass

def sendRegistrationTelegram(tg_name):
    if TelegramSettings.objects.get(pk=2):
        settings = TelegramSettings.objects.get(pk=2)
        token = str(settings.tg_token)
        chat_id = str(tg_name)
        text = str(settings.tg_message)
        api = "https://api.telegram.org/bot"+token+"/sendMessage"
        text = text + tg_name + "\n" 
        try:
            req = requests.post(api, data={
                'chat_id':chat_id,
                'text':text
            })
        except:
            pass
        finally:
            if req.status_code != 200:
                print("Error. "+req)
            elif req.status_code == 500:
                print("Server Error")
            else:
                print("Success")

    else:
        pass