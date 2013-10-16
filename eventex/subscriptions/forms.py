# coding: utf-8
from django import forms
from django.forms import TextInput
from django.forms import MultiWidget, MultiValueField
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from eventex.subscriptions.models import Subscription


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))
    if len(value) != 11:
        raise ValidationError(_(u'CPF deve conter 11 dígitos'))
 

class PhoneWidget(forms.MultiWidget):
    def __init__(self, **kwargs):
        widgets = (forms.TextInput(attrs={'class': 'form-control'}),
                   forms.TextInput(attrs={'class': 'form-control'}))
        super(PhoneWidget, self).__init__(widgets, **kwargs)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')


class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (forms.IntegerField(),
                  forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if not data_list:
            return ''
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'DDD inválido.'))
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'Número inválido.'))
        return '%s-%s' % tuple(data_list)



class SubscriptionForm(forms.ModelForm):
    phone = PhoneField(label=_('Telefone'), required=False)

    class Meta:
        model = Subscription
        fields = ('name', 'cpf', 'email', 'phone')
        exclude = ('paid',)
        widgets = {'name': TextInput(attrs={'class': 'form-control'}),
                   'cpf': TextInput(attrs={'class': 'form-control'}),
                   'email': TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].validators.append(CPFValidator)


    def clean_name(self):
        name = self.cleaned_data['name']
        words = name.split()
        for index, word in enumerate(words):
            words[index] = word.capitalize()
        capitalized_name = ' '.join(words)
        return capitalized_name


    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise ValidationError(_(u'Informe seu email ou telefone'))
        return self.cleaned_data
