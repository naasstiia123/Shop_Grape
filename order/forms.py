from django import forms
from .models import Order, City, Department, PayMethod

class OrderForm(forms.ModelForm):

    name = forms.CharField(max_length=50, label='Імя', widget=forms.TextInput(attrs={'type': "text",
                                                                                     'name': "name",
                                                                                     'class': "form-control",
                                                                                     'id': "name",
                                                                                     'placeholder': "Ім'я",
                                                                                     'data-rule': "minlen:4",
                                                                                     'data-msg': "Please enter at least 4 "
                                                                                                 "chars"}))

    last_name = forms.CharField(max_length=50, label='Прізвище', widget=forms.TextInput(attrs={'type': "text",
                                                                                               'name': "last_name",
                                                                                               'class': "form-control",
                                                                                               'id': "name",
                                                                                               'placeholder': "Прізвище",
                                                                                               'data-rule': "minlen:4",
                                                                                               'data-msg': "Please enter at least "
                                                                                                           "4 chars"}))

    email = forms.EmailField(max_length=100, label='Email', widget=forms.EmailInput(attrs={'type': "email",
                                                                                        'name': "email",
                                                                           'class': "form-control",
                                                                           'id': "email",
                                                                           'placeholder': "Email",
                                                                           'data-rule': "email",
                                                                           'data-msg': "Please enter a valid "
                                                                                       "email"}))

    phone = forms.CharField(max_length=16, label='Номер телефону', widget=forms.TextInput(attrs={'type':
                                                                                                                 "text",
                                                                                                 'class': "form-control",
                                                                                                 'name': "phone",
                                                                                                 'id': "phone",
                                                                                                 'placeholder': "Номер телефону",
                                                                                                 'data-rule': "minlen:4",
                                                                                                 'data-msg': "Please enter at least 4 "
                                                                                                             "chars"}))

    city = forms.ModelChoiceField(queryset=City.objects.filter(is_visible=True), label='Місто')

    department = forms.ModelChoiceField(queryset=Department.objects.filter(is_visible=True),
    label='Відділення пошти',)

    pay_method = forms.ModelChoiceField(queryset=PayMethod.objects.filter(is_visible=True), label='Спосіб оплати')

    class Meta:

        model = Order
        fields = ['name', 'last_name', 'email',
                  'phone', 'city', 'department', 'pay_method']
