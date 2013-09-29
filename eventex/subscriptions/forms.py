# coding: utf-8
from django import forms
from django.forms import TextInput
from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('name', 'cpf', 'email', 'phone')
        exclude = ('paid',)
        widgets = {'name': TextInput(attrs={'class': 'form-control'}),
                   'cpf': TextInput(attrs={'class': 'form-control'}),
                   'email': TextInput(attrs={'class': 'form-control'}),
                   'phone': TextInput(attrs={'class': 'form-control'})}

