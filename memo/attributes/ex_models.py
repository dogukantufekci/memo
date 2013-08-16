# class ml1000CharVA(AbstractAttribute):
#     created_by = models.ForeignKey(
#         User,
#         related_name='ml1000_char_v_as_created_by',
#     )
#     created_via = models.ForeignKey(
#         App,
#         related_name='ml1000_char_v_as_created_via',
#     )

#     object = models.ForeignKey(
#         Object,
#         related_name='ml1000_char_v_as_object',
#     )
#     key = models.ForeignKey(
#         Key,
#         related_name='ml1000_char_v_as_key',
#     )
#     value = models.CharField(
#         max_length=1000,
#     )

#     def __unicode__(self):
#         return u"<ml1000CharVA: %s - %s's %s is %r>" % (
#             self.id,
#             self.object.get_title(),
#             self.key.title,
#             self.value[:100],
#         )

# class BigIntegerVA(AbstractAttribute):
#     created_by = models.ForeignKey(
#         User,
#         related_name='big_integer_v_as_created_by',
#     )
#     created_via = models.ForeignKey(
#         App,
#         related_name='big_integer_v_as_created_via',
#     )

#     object = models.ForeignKey(
#         Object,
#         related_name='big_integer_v_as_object',
#     )
#     key = models.ForeignKey(
#         Key,
#         related_name='big_integer_v_as_key',
#     )
#     value = models.BigIntegerField()

#     def __unicode__(self):
#         return u"<BigIntegerVA: %s - %s's %s is %r>" % (
#             self.id,
#             self.object.get_title(),
#             self.key.title,
#             self.value
#         )