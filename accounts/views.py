from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .form import UserSignUpForm
from .form import UserSignUpFormTelegram
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site 
from .models import Profile
from telegramBot.sendmessage import sendRegistrationTelegram
 
def getUserIp(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def signup(request):
    render(request, 'registration/signup.html', {'formTelegram':UserSignUpFormTelegram,'form': UserSignUpForm()})

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        # and request.recaptcha_is_valid
        if form.is_valid() :  
            telegram_name = request.POST['telegram_name']
            site = get_current_site(request) 
            user = form.save(commit=False)
            user.is_active = False
            user.save() 

            profile = Profile.objects.create(user=user)
            profile.ip_user = getUserIp(request)
            profile.telegram_name = telegram_name
            profile.save()

            sendRegistrationTelegram(tg_name=telegram_name)
            
        else:
            return render(request, 'registration/signup.html', {'formTelegram':UserSignUpFormTelegram,'form': form})
    return render(request, 'registration/signup.html', {'formTelegram':UserSignUpFormTelegram,'form': UserSignUpForm()})
# class SignUpView(generic.CreateView):
#     form_class = UserSignUpForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'