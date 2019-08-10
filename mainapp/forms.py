from django import forms
from .models import ContractUs

class ContractUsForm(forms.ModelForm):
    class Meta:
        model = ContractUs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContractUsForm, self).__init__(*args, **kwargs)

        # sets the placeholder key/value in the attrs for a widget
        # when the form is instantiated (so the widget already exists)
        self.fields['user_name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['user_email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['user_subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['user_message'].widget.attrs['placeholder'] = 'Message'