# coding: utf-8 
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerDetail(TestCase):
    def setUp(self):
        Speaker.objects.create(name='Filipe Manuel',
                               slug='filipe-manuel',
                               url='http://github.com/filipemanuelofs',
                               description='Lorem Ipsum')

        url = r('core:speaker_detail', kwargs={'slug': 'filipe-manuel'})
        self.resp = self.client.get(url)

    def test_get(self):
        """
        GET should result in 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Template should be core/speaker_detail.html
        """
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        """
        HTML must contains
        """
        self.assertContains(self.resp, 'Filipe Manuel')
        self.assertContains(self.resp, 'Lorem Ipsum')
        self.assertContains(self.resp, 'http://github.com/filipemanuelofs')

    def test_context(self):
        """
        Speaker must be in context
        """
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'linus-linux'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)