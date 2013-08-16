# from django.db import models
# from django.contrib.auth.models import User

# from apps.models import App
# from objects.models import Object


# class Verb(models.Model):
#     created_by = models.ForeignKey(
#         User,
#         related_name='verbs_created_by',
#     )
#     created_on = models.DateTimeField(
#         auto_now_add=True,
#     )
#     created_via = models.ForeignKey(
#         App,
#         related_name='verbs_created_via',
#     )

#     key = models.CharField(
#         max_length=100,
#         unique=True,
#     )
#     infinitive_form = models.CharField(
#         db_index=True,
#         max_length=100,
#     )
#     past_form = models.CharField(
#         max_length=100,
#     )
#     present_form = models.CharField(
#         max_length=100,
#     )
#     present_continuous_form = models.CharField(
#         max_length=100,
#     )
#     future_form = models.CharField(
#         max_length=100,
#     )

#     def __unicode__(self):
#         return u'<Verb: %s - %s - %s>' % (
#             self.id,
#             self.key,
#             self.base_form,
#         )


# class Action(models.Model):
#     created_by = models.ForeignKey(
#         User,
#         related_name='actions_created_by',
#     )
#     created_on = models.DateTimeField(
#         auto_now_add=True,
#     )
#     created_via = models.ForeignKey(
#         App,
#         related_name='actions_created_via',
#     )

#     subject = models.ForeignKey(
#         Object,
#         related_name='actions_subject',
#     )
#     verb = models.ForeignKey(
#         Verb,
#         related_name='actions_verb',
#     )
#     quantity = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='actions_quantity',
#     )
#     object = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='actions_object',
#     )
#     manner = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='actions_manner',
#     )
#     place = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='actions_place',
#     )
#     time = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='actions_time',
#     )

#     def __unicode__(self):
#         return u'<Action: %s - %s %s %s %s %s %s %s>' % (
#             self.id,
#             self.subject.get_title(),
#             self.verb.infinitive_form,
#             self.quantity.get_title() or '',
#             self.object.get_title() or '',
#             self.manner.get_title() or '',
#             ('at %s' % self.place.get_title()) or '',
#             ('at %s' % self.time.get_title()) or '',
#         )