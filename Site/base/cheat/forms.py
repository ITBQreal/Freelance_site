from django import forms
from .models import Channel, Streams, BotAccounts, Binds


class ChannelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChannelForm, self).__init__(*args, **kwargs)
        self.fields['channel_name'].error_messages = {'required': ''}

    class Meta:
        model = Channel
        fields = ['channel_name']
        labels = {'channel_name': ''}
        widgets = {
            'channel_name': forms.TextInput(attrs={'style': 'width: 100px;'}),
        }


class StreamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StreamForm, self).__init__(*args, **kwargs)
        self.fields['stream_url'].error_messages = {'required': 'QWEWQEQWEWQE'}

    class Meta:
        model = Streams
        fields = ['stream_url']
        labels = {'stream_url': ''}
        widgets = {
            'stream_url': forms.TextInput(attrs={'style': 'width: 100px;'}),
        }

class BotForm(forms.ModelForm):
    class Meta:
        model = BotAccounts
        fields = ['login', 'password', 'owner']
        labels = {'login': 'Login', 'password':'Password', 'owner':'Owner'}
        widgets = {
            'login': forms.TextInput(attrs={'style': 'width: 100px;'}),
            'password': forms.TextInput(attrs={'style': 'width: 100px;'}),
            'owner': forms.Select(),
        }

class BindForm(forms.ModelForm):
    class Meta:
        model = Binds
        fields = ['name', 'text']
        labels = {'name': 'Bind name', 'text':'Bind text'}
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100px;'}),
            'text': forms.TextInput(attrs={'style': 'width: 100px;'}),
        }