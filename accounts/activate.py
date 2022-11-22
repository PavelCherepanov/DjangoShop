from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
User = get_user_model()


@require_http_methods(["GET"])
def activate(request, uidb64, token):
    print("request")
    print(request)
    print("uid64")
    print(uidb64)
    print("token")
    print(token)
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    print(user)
    print(user.pk)
    print()
    print(account_activation_token.check_token(user, token))
    print(user is not None)
    if user is not None: #and account_activation_token.check_token(user, token): 
        user.is_active = True  
        user.profile.email_confirmed = True 
        user.save()
        login(request, user)
    else:
        print("Error with token")

    return redirect('/home')