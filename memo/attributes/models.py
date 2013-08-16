from django.db import models
from django.contrib.auth.models import User

from apps.models import App
from memo.models import ModelMeta
from objects.models import Object


class Key(ModelMeta):
    created_by = models.ForeignKey(
        User,
        related_name='keys_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='keys_created_via',
    )

    key = models.CharField(
        max_length=50,
        unique=True,
    )
    title = models.CharField(
        db_index=True,
        max_length=100,
    )

    def __unicode__(self):
        return u'<Key: %s - %s - %s>' % (
            self.id,
            self.key,
            self.title,
        )


class AbstractAttribute(ModelMeta):
    date_from = models.DateTimeField(
        blank=True,
        null=True,
    )
    date_to = models.DateTimeField(
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


# Object Value Attribute ----------------------------


class ObjectVA(AbstractAttribute):
    created_by = models.ForeignKey(
        User,
        related_name='object_v_as_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='object_v_as_created_via',
    )

    object = models.ForeignKey(
        Object,
        related_name='object_v_as_object',
    )
    key = models.ForeignKey(
        Key,
        related_name='object_v_as_key',
    )
    value = models.ForeignKey(
        Object,
        related_name='object_v_as_value',
    )

    def __unicode__(self):
        return u"<ObjectVA: %s - %s's %s is %s>" % (
            self.id,
            self.object.get_title(),
            self.key.title,
            self.value.get_title(),
        )


# Digital Object Value Attribute ----------------------------


class DecimalVA(AbstractAttribute):
    created_by = models.ForeignKey(
        User,
        related_name='decimal_v_as_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='decimal_v_as_created_via',
    )

    object = models.ForeignKey(
        Object,
        related_name='decimal_v_as_object',
    )
    key = models.ForeignKey(
        Key,
        related_name='decimal_v_as_key',
    )
    value = models.DecimalField(
        decimal_places=10,
        max_digits=30,
    )

    def __unicode__(self):
        return u"<DecimalVA: %s - %s's %s is %r>" % (
            self.id,
            self.object.get_title(),
            self.key.title,
            self.value
        )


class TextVA(AbstractAttribute):
    created_by = models.ForeignKey(
        User,
        related_name='text_v_as_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='text_v_as_created_via',
    )

    object = models.ForeignKey(
        Object,
        related_name='text_v_as_object',
    )
    key = models.ForeignKey(
        Key,
        related_name='text_v_as_key',
    )
    value = models.TextField()

    def __unicode__(self):
        return u"<TextVA: %s - %s's %s is %r>" % (
            self.id,
            self.object.get_title(),
            self.key.title,
            self.value[:100],
        )