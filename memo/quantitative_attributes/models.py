from django.db import models
from django.contrib.auth.models import User

from apps.models import App
from attributes.models import Key, AbstractAttribute
from objects.models import Object


class DecimalQQA(AbstractAttribute):
    created_by = models.ForeignKey(
        User,
        related_name='decimal_q_q_as_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='decimal_q_q_as_created_via',
    )

    object = models.ForeignKey(
        Object,
        related_name='decimal_q_q_as_object',
    )
    key = models.ForeignKey(
        Key,
        related_name='decimal_q_q_as_key',
    )
    quantity = models.DecimalField(
        decimal_places=10,
        max_digits=30,
    )
    units = models.ForeignKey(
        Object,
        related_name='decimal_q_q_as_units',
    )

    def __unicode__(self):
        return u"<DecimalQQA: %s - %s's %s is %s %s>" % (
            self.id,
            self.object.get_title(),
            self.key.title,
            self.quantity,
            self.units.get_title(),
        )