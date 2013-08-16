from django.db import models


class ModelMeta(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True