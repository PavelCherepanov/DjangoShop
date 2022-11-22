from .form import UserSignUpForm
from .form import UserSignUpFormTelegram
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site 
from django.contrib.auth.decorators import login_required
from telegramBot.sendmessage import sendRegistrationTelegram
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.views.decorators.http import require_http_methods
from accounts.tokens import account_activation_token
 
def getUserIp(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
    
@require_http_methods(["GET", "POST"])
def signup(request):
    render(request, 'registration/signup.html', {'formTelegram':UserSignUpFormTelegram,'form': UserSignUpForm()})

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        # formT = UserSignUpFormTelegram(request.POST, instance=request.user.profile)
        # and request.recaptcha_is_valid
        if form.is_valid() :  
            user = form.save()
            telegram_name = request.POST['telegram_name']
            site = get_current_site(request) 
            user.is_active = False
            user.profile.ip_user = getUserIp(request)
            user.profile.telegram_name = telegram_name
            user.save() 
            message = 'http://' + site.domain + '/activate/'+ urlsafe_base64_encode(force_bytes(user.pk)) + "/" + account_activation_token.make_token(user)
            sendRegistrationTelegram(tg_name=telegram_name, tg_message=message)
        else:
            return render(request, 'registration/signup.html', {'formTelegram':UserSignUpFormTelegram,'form': form})
    return render(request, 'registration/signup.html', {'formTelegram':UserSignUpFormTelegram,'form': UserSignUpForm()})

@login_required
def profile(request):
	return render(request, 'registration/profile.html')