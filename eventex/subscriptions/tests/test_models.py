# coding: utf-8
from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.object = Subscription(
            name='Filipe Manuel',
            cpf='06616141403',
            email='kind76@gmail.com',
            phone='82-96427829'
        )

    def test_create(self):
        """
        Subscription must have name, cpf, email and phone
        """
        self.object.save()
        self.assertEqual(1, self.object.id)

    def test_has_created_at(self):
        """
        Subscription must have automatic created_at
        """
        self.object.save()
        self.assertIsInstance(self.object.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Filipe Manuel', unicode(self.object))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        """
        Create a first entry to force colision
        """
        Subscription.objects.create(name='Filipe Manuel',
                                    cpf='06616141403',
                                    email='kind76@gmail.com',
                                    phone='82-96427829')

    def test_cpf_unique(self):
        """
        CPF must be unique
        """
        s = Subscription(name='Filipe Manuel',
                         cpf='06616141403',
                         email='outro@gmail.com',
                         phone='82-96427829')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        """
        Email must be unique
        """
        s = Subscription(name='Filipe Manuel',
                         cpf='05487856932',
                         email='kind76@gmail.com',
                         phone='82-96427829')
        self.assertRaises(IntegrityError, s.save)
