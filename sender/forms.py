from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField, TextInput

from sender.models import Mailing


class MailingForm(ModelForm):

    class Meta:
        model = Mailing
        fields = ('title', 'body')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(MailingForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(MailingForm, self).clean()
        body = cleaned_data.get("body")
        if not body:
            msg = "Please, enter body content"
            self.add_error('body', msg)
