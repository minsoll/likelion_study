from django import forms
from .models import Country

class CountryWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CountryWriteForm, self).__init__(*args, **kwargs)
        self.fields['country'].label = '나라'

    class Meta:
        model = Country
        fields = ['country',]