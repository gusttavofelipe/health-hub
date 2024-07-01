from django import forms
from records.models import PersonalHealthRecord


class PersonalHealthRecordForm(forms.ModelForm):
    class Meta:
        model = PersonalHealthRecord
        fields = "__all__"
