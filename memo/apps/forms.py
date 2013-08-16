from django import forms

from .models import App


class AppForm(forms.ModelForm):

    secret = forms.CharField(
        help_text='Exactly %s characters or new secret will be generated.' % App.SECRET_MAX_LENGTH,
        max_length=App.SECRET_MAX_LENGTH,
        required=False,
    )

    class Meta:
        model = App

    def save(self, commit=True):
        app = super(AppForm, self).save(commit=False)
        if not (
            app.secret and 
            App.validate_secret_length(app.secret)
        ):
            app.secret = App.generate_secret()
        if commit:
            app.save()
        return app