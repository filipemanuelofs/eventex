# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager


class Speaker(models.Model):
    name = models.CharField(_(u'Nome'), max_length=255)
    slug = models.SlugField(_(u'Slug'))
    url = models.URLField(_(u'URL'))
    description = models.TextField(_(u'Descrição'), blank=True)

    class Meta:
        verbose_name = _(u'palestrante')
        verbose_name_plural = _(u'palestrantes')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('Email')),
        ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_(u'palestrante'))
    kind = models.CharField(_(u'Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_(u'Valor'), max_length=255)

    objects = models.Manager()
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')

    def __unicode__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_(u'palestrante'))

    class Meta:
        verbose_name = _(u'palestra')
        verbose_name_plural = _(u'palestras')

    def __unicode__(self):
        return self.title

    objects = PeriodManager()
    
    # @models.permalink
    def get_absolute_url(self):
        # return ('core:talk_list', (), {'pk': self.pk})
        return '/palestras/%d/' % self.pk