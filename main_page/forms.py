from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    name = forms.CharField(max_length=50, label='Ім\'я', widget=forms.TextInput(attrs={'type': "text",
                                                                                       'name': "name",
                                                                                       'class': "form-control",
                                                                                       'id': "name",
                                                                                       'placeholder': "Your Name",
                                                                                       'data-rule': "minlen:4",
                                                                                       'data-msg': "Please enter at least 4 chars"}))
    message = forms.CharField(max_length=300, label='Відгук', widget=forms.TextInput(attrs={'class': "form-control",
                                                                                            'name': "message",
                                                                                            'rows': "5",
                                                                                            'placeholder': "Message"}))


    class Meta:
        model = Feedback
        fields = ['name', 'message']
