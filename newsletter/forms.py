from django import forms
from crispy_forms.helper import FormHelper
from .models import Newsletter


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False

    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email
