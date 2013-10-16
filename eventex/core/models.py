# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('URL'))
    description = models.TextField(_('Descrição'), blank=True)
    
    class Meta:
        verbose_name = _('Speaker')
        verbose_name_plural = _('Speakers')

    def __unicode__(self):
        return self.name