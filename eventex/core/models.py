# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('URL'))
    description = models.TextField(_('Descrição'), blank=True)

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('Email')),
        ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_(u'palestrante'))
    kind = models.CharField(_('Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('Valor'), max_length=255)

    def __unicode__(self):
        return self.value