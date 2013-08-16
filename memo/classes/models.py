from django.db import models
from django.contrib.auth.models import User

from apps.models import App
from memo.models import ModelMeta
from objects.models import Object


class Class(ModelMeta):
    created_by = models.ForeignKey(
        User,
        related_name='classes_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='classes_created_via',
    )

    object = models.ForeignKey(
        Object,
        related_name='classes_object',
    )
    _class = models.ForeignKey(
        Object,
        related_name='classes_class',
    )
    date_from = models.DateTimeField(
        blank=True,
        null=True,
    )
    date_to = models.DateTimeField(
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return u'<Class: %s - %s is %s>' % (
            self.id,
            self.object.get_title(),
            self._class.get_title(),
        )

    class Meta:
        verbose_name_plural = 'classes'