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
