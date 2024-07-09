from django import forms
from professional.models import Professional


class PersonalHealthRecordForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ["full_name", "phone_number", "email", "birth_date"]
