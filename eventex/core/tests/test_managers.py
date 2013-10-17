# coding: utf-8 
from django.test import TestCase
from eventex.core.models import Contact, Speaker, Talk


class ContactManager(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Filipe Manuel', slug='filipe-manuel', 
                                   url='http://github.com/filipemanuelofs')

        s.contact_set.add(Contact(kind='E', value='kind76@gmail.com'),
                          Contact(kind='P', value='82-96427829'),
                          Contact(kind='F', value='82-12345678'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: kind76@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 82-96427829>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 82-12345678>']
        self.assertQuerysetEqual(qs, expected)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        """
        Should return only talks before 12h
        """
        self.assertQuerysetEqual(Talk.objects.at_morning(),
                                 ['Morning Talk'], 
                                 lambda t: t.title)

    def test_afternoon(self):
        """
        Should return only talks after 11:59:59
        """
        self.assertQuerysetEqual(Talk.objects.at_afternoon(),
                                 ['Afternoon Talk'], 
                                 lambda t: t.title)