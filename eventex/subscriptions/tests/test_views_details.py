# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Filipe Manuel',
                                        cpf='06616141403',
                                        email='kind76@gmail.com',
                                        phone='82-96427829')
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))

    def test_get(self):
        """
        GET /inscricao/1/ should return status code 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Must return used template
        """
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        """
        Context must have a subscription instance.
        """
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        """
        Check if subscription data was rendered
        """
        self.assertContains(self.resp, 'Filipe Manuel')


class DetailNotFound(TestCase):
    def test_not_found(self):
        """
        Must return 404 if detail not found
        """
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
