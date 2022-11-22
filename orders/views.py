from django.shortcuts import render, redirect
from .cryptocloud import CryptoCloud
from .qiwi import Qiwi
from cart.views import getTotalPrice
from .form import OrderForm

def checkout(request):
    if request.user.is_authenticated:
        render(request, "checkout.html", {'form': OrderForm()})
        if request.method == "POST":
            form = OrderForm(request.POST)
            print(form)
            if form.is_valid():
                order = form.save()
                order.user = request.user
                order.paid = False
                order.save()
                if request.POST.get('cash') == 'on':
                    return redirect("/home")
                elif request.POST.get('qiwi') == 'on':
                    qiwi = Qiwi(request, getTotalPrice(request))
                    return redirect(qiwi.createInvoice())
                elif request.POST.get('crypto') == 'on':
                    crypto = CryptoCloud(getTotalPrice(request), str(order.id))
                    return redirect(crypto.createInvoice())
                else:
                    print("Error")
            else:
                return render(request, "checkout.html", {'form':form})
    else:
        return redirect("/accounts/signup/")
    return render(request, "checkout.html", {'form': OrderForm()})
def generateOrderId():
    pass        