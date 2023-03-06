from .models import Category_good, Phone, Email_adress, Address


def getting_category(request):
    """
        Allow to show categories of goods in every template.
     """
    category = Category_good.objects.filter(is_visible=True)
    return {'category': category, }

def getting_number(request):
    """
            Allow to show contacts in every template.
    """
    phone = Phone.objects.filter(is_visible=True)
    return {'phone': phone, }

def getting_mail(request):
    """
                Allow to show contacts in every template.
    """
    mails = Email_adress.objects.filter(is_visible=True)
    return {'mails': mails, }

def getting_address(request):
    """
                Allow to show contacts in every template.
    """
    location = Address.objects.filter(is_visible=True)
    return {'location': location, }
