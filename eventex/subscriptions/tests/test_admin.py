from django.test import TestCase
from mock import Mock
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin


class MarkAsPaid(TestCase):
    def setUp(self):
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        Subscription.objects.create(name='Filipe Manuel',
                                    cpf='06616141403',
                                    email='kind76@gmail.com',
                                    phone='82-96427829')

    def test_has_action(self):
        """
        Action is created
        """
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())