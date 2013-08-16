from django.db import models
from django.contrib.auth.models import User

from apps.models import App
from memo.models import ModelMeta


class Object(ModelMeta):
    created_by = models.ForeignKey(
        User,
        related_name='objects_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='objects_created_via',
    )

    title = models.CharField(
        blank=True,
        db_index=True,
        max_length=100,
    )

    def get_title(self):
        return self.title or 'Untitled'

    def __unicode__(self):
        return u'<Object: %s - %s>' % (
            self.id,
            self.get_title(),
        )