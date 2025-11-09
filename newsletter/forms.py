from django import forms
from crispy_forms.helper import FormHelper
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    helper = FormHelper()
    helper.for_show_labels = False

    class Meta:
        model = Newsletter
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email
