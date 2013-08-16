# from django.db import models
# from django.contrib.auth.models import User

# from actions.models import Verb
# from apps.models import App
# from objects.models import Object


# class Activity(models.Model):
#     created_by = models.ForeignKey(
#         User,
#         related_name='activities_created_by',
#     )
#     created_on = models.DateTimeField(
#         auto_now_add=True,
#     )
#     created_via = models.ForeignKey(
#         App,
#         related_name='activities_created_via',
#     )

#     date_from = models.DateTimeField(
#         blank=True,
#         null=True,
#     )
#     date_to = models.DateTimeField(
#         blank=True,
#         null=True,
#     )
#     date_to_present = models.NullBooleanField()

#     subject = models.ForeignKey(
#         Object,
#         related_name='activities_subject',
#     )
#     verb = models.ForeignKey(
#         Verb,
#         related_name='activities_verb',
#     )
#     quantity = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='activities_quantity',
#     )
#     object = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='activities_object',
#     )
#     manner = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='activities_manner',
#     )
#     place = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='activities_place',
#     )
#     time = models.ForeignKey(
#         Object,
#         blank=True,
#         null=True,
#         related_name='activities_time',
#     )

#     def __unicode__(self):
#         return u'<Activity: %s - %s %s %s %s %s %s %s>' % (
#             self.id,
#             self.subject.get_title(),
#             self.verb.infinitive_form,
#             self.quantity.get_title() or '',
#             self.object.get_title() or '',
#             self.manner.get_title() or '',
#             ('at %s' % self.place.get_title()) or '',
#             ('at %s' % self.time.get_title()) or '',
#         )

#     class Meta:
#         verbose_name_plural = 'activities'