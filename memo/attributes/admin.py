from django.contrib import admin

from .models import (
    Key,
    ObjectVA,
    DecimalVA,
    TextVA,
)


admin.site.register(Key)
admin.site.register(ObjectVA)
admin.site.register(DecimalVA)
admin.site.register(TextVA)