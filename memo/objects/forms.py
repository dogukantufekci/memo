from django import forms

from .models import (
    Attribute,
    Class,
    CountableAttribute,
    CountableIntervallicAttribute,
    Instance,
    IntervallicAttribute,
    Key,
)


class AttributeForm(forms.ModelForm):

    def __init__(self, user, app, *args, **kwargs):
        self.o = Object.objects.create(
            created_by=user,
            created_via=app,
            type=1,
        )
        super(AttributeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Attribute


class ClassForm(forms.ModelForm):

    def __init__(self, user, app, *args, **kwargs):
        self.o = Object.objects.create(
            created_by=user,
            created_via=app,
            type=2,
        )
        super(ClassForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Class


class CountableAttributeForm(forms.ModelForm):

    def __init__(self, user, app, *args, **kwargs):
        self.o = Object.objects.create(
            created_by=user,
            created_via=app,
            type=3,
        )
        super(CountableAttributeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CountableAttribute


class CountableIntervallicAttributeForm(forms.ModelForm):

    def __init__(self, user, app, *args, **kwargs):
        self.o = Object.objects.create(
            created_by=user,
            created_via=app,
            type=4,
        )
        super(CountableIntervallicAttributeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CountableIntervallicAttribute


class InstanceForm(forms.ModelForm):

    def __init__(self, user, app, *args, **kwargs):
        self.o = Object.objects.create(
            created_by=user,
            created_via=app,
            type=5,
        )
        super(InstanceForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Instance


class IntervallicAttributeForm(forms.ModelForm):

    def __init__(self, user, app, *args, **kwargs):
        self.o = Object.objects.create(
            created_by=user,
            created_via=app,
            type=6,
        )
        super(IntervallicAttributeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = IntervallicAttribute


class KeyForm(forms.ModelForm):

    def __init__(self, user, app, *args, **kwargs):
        self.o = Object.objects.create(
            created_by=user,
            created_via=app,
            type=7,
        )
        super(KeyForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Key


# class ObjectForm(forms.ModelForm):

#     class Meta:
#         model = Object

#     error_messages = {
#         'type_not_permitted': ("Only <Class> nd <Instance> type objects "
#                                "are allowed in this form.")
#     }

#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super(ObjectForm, self).__init__(*args, **kwargs)

#     def clean(self):
#         PERMITTED_TYPES = (5,6,)

#         if self.cleaned_data['type'] not in PERMITTED_TYPES:
#             raise forms.ValidationError(
#                 self.error_messages['type_not_permitted']
#             )

#     def save(self, commit=True):
#         app = super(AppForm, self).save(commit=False)
#         if not (
#             app.secret and 
#             App.validate_secret_length(app.secret)
#         ):
#             app.secret = App.generate_secret()
#         if commit:
#             app.save()
#         return app