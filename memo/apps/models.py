from django.db import models
from django.contrib.auth.models import User

from memo import tools
from memo.models import ModelMeta


class App(ModelMeta):
    SECRET_MAX_LENGTH = 10

    created_by = models.ForeignKey(
        User,
        related_name='apps_created_by',
    )

    secret = models.CharField(
        max_length=SECRET_MAX_LENGTH,
        unique=True,
    )
    title = models.CharField(
        db_index=True,
        max_length=100,
    )

    def __unicode__(self):
        return u'<App: %s - %s>' % (self.id, self.title)

    @staticmethod
    def validate_secret_length(secret):
        return len(secret) == App.SECRET_MAX_LENGTH

    @staticmethod
    def validate_secret_uniqueness(secret):
        return App.objects.filter(secret=secret).count() == 0

    @staticmethod
    def validate_secret(secret):
        return (
            App.validate_secret_length(secret) and
            App.validate_secret_uniqueness(secret)
        )

    @staticmethod
    def generate_secret():
        secret = tools.generate_key(length=App.SECRET_MAX_LENGTH)
        while not App.validate_secret(secret):
            secret = tools.generate_key(length=App.SECRET_MAX_LENGTH)
        return secret