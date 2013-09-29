# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_fields(self):
        """
        Form must have 4 fields
        """
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)


    def test_cpf_is_digit(self):
        """
        CPF must only accept digits
        """
        form = self.make_validated_form(cpf = 'ABCD5678901')
        self.assertItemsEqual(['cpf'], form.errors)


    def test_cpf_has_11_digits(self):
        """
        CPF must have 11 digits
        """
        form = self.make_validated_form(cpf = '1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        """
        Email is optional
        """
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Filipe Manuel',
                    cpf='06616141403',
                    email='kind76@gmail.com',
                    phone='82-96427829')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
