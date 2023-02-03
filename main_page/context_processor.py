from .models import Category_good, Phone, Email_adress, Address


def getting_category(request):
    category = Category_good.objects.filter(is_visible=True)
    return {'category': category}

def getting_number(request):
    phone = Phone.objects.filter(is_visible=True)
    return {'phone': phone}

def getting_mail(request):
    mails = Email_adress.objects.filter(is_visible=True)
    return {'mails': mails}

def getting_address(request):
    location = Address.objects.filter(is_visible=True)
    return {'location': location}
