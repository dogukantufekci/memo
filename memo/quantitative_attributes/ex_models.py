class BigIntegerQQA(AbstractAttribute):
    created_by = models.ForeignKey(
        User,
        related_name='big_integer_q_q_as_created_by',
    )
    created_via = models.ForeignKey(
        App,
        related_name='big_integer_q_q_as_created_via',
    )

    object = models.ForeignKey(
        Object,
        related_name='big_integer_q_q_as_object',
    )
    key = models.ForeignKey(
        Key,
        related_name='big_integer_q_q_as_key',
    )
    quantity = models.BigIntegerField()
    units = models.ForeignKey(
        Object,
        related_name='big_integer_q_q_as_units',
    )

    def __unicode__(self):
        return u"<BigIntegerQQA: %s - %s's %s is %s %s>" % (
            self.id,
            self.object.get_title(),
            self.key.title,
            self.quantity,
            self.units.get_title(),
        )