from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class RegistrationForm(forms.ModelForm):

    """
    Form to registration on the site.
    """

    class Meta:
        model = User
        fields = ('username', 'email',)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        'class': "form-control",
        'placeholder': "Name"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': "email",
        'class': "form-control",
        'placeholder': "Email"
    }))
    password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(attrs={
        'type': "password",
        'class': "form-control",
        'placeholder': "Password"
    }))
    password2 = forms.CharField(label='Repeat password', min_length=8, widget=forms.PasswordInput(attrs={
        'type': "password2",
        'class': "form-control",
        'placeholder': "Password"
    }))

    def clean_password2(self):
        """
        Compare entered passwords and return error if not correspondence.
        :return:password or error

        """
        data = self.cleaned_data
        if data['password'] == data['password2']:
            return data['password2']
        raise forms.ValidationError('Passwords don\'t match.')


class LoginForm(forms.Form):
    """
    Form to log in on the site.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
                                                    'type': "text",
                                                    'class': "form-control",
                                                    'placeholder': "Name"
                                                }))

    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
                                                    'type': "password",
                                                    'class': "form-control",
                                                    'placeholder': "Password"
                                                }))

    def clean(self):
        """
        Check entered login and password for registration and correspondence.
        :return:cleaned form or error

        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('login or password is uncorect')
        return super().clean()
