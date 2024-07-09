from django import forms
from professional.models import Professional


class ProfessionalForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirm password", widget=forms.PasswordInput
    )

    class Meta:
        model = Professional
        fields = [
            "full_name",
            "phone_number",
            "email",
            "birth_date",
            "password",
            "confirm_password",
        ]
